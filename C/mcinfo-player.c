#include <stdio.h>
#include <stdlib.h>
#include <curl/curl.h>
#include <string.h>
#include "cJSON/cJSON.h"
#include "base64/base64.h"

struct string
{
	char *ptr;
	size_t len;
};

void initString(struct string *s)
{
	s->len = 0;
	s->ptr = malloc(s->len + 1);
	s->ptr[0] = '\0';
}

size_t writefunc(void *ptr, size_t size, size_t nmemb, struct string *s)
{
	size_t new_len = s->len + size * nmemb;
	s->ptr = realloc(s->ptr, new_len + 1);
	memcpy(s->ptr + s->len, ptr, size * nmemb);
	s->ptr[new_len] = '\0';
	s->len = new_len;

	return size * nmemb;
}

char *getData(char *url)
{
	CURLcode ret;
	CURL *hnd;
	char *data;
	struct string s;
	initString(&s);

	hnd = curl_easy_init();
	curl_easy_setopt(hnd, CURLOPT_BUFFERSIZE, 102400L);
	curl_easy_setopt(hnd, CURLOPT_URL, url);
	curl_easy_setopt(hnd, CURLOPT_NOPROGRESS, 1L);
	curl_easy_setopt(hnd, CURLOPT_USERAGENT, "curl/7.68.0");
	curl_easy_setopt(hnd, CURLOPT_MAXREDIRS, 50L);
	curl_easy_setopt(hnd, CURLOPT_HTTP_VERSION, (long)CURL_HTTP_VERSION_2TLS);
	curl_easy_setopt(hnd, CURLOPT_FTP_SKIP_PASV_IP, 1L);
	curl_easy_setopt(hnd, CURLOPT_TCP_KEEPALIVE, 1L);
	curl_easy_setopt(hnd, CURLOPT_WRITEFUNCTION, writefunc);
	curl_easy_setopt(hnd, CURLOPT_WRITEDATA, &s);

	ret = curl_easy_perform(hnd);

	curl_easy_cleanup(hnd);
	hnd = NULL;

	return s.ptr;
	free(s.ptr);
}

char *humanReadableTime(time_t timestamp)
{
	char *buff = malloc(128);
	struct tm *tm;

	tm = gmtime(&timestamp);
	snprintf(buff, 128, "%d-%d-%d %d:%d:%d", tm->tm_year + 1900, tm->tm_mon, tm->tm_mday, tm->tm_hour, tm->tm_min, tm->tm_sec);

	return buff;
}

int main()
{
	cJSON *current_element = NULL;
	char username[32];
	char url[256];
	char timeBuff[32];

	printf("Username: ");
	if (scanf("%s", username) == EOF)
	{
		return -1;
	}

	printf("Gathering some data...\n");

	snprintf(url, sizeof url, "https://api.mojang.com/users/profiles/minecraft/%s", username);
	cJSON *nu = cJSON_Parse(getData(url));
	strcpy(username, cJSON_GetObjectItem(nu, "name")->valuestring);
	char *uuid = cJSON_GetObjectItem(nu, "id")->valuestring;

	snprintf(url, sizeof url, "https://api.mojang.com/user/profiles/%s/names", uuid);
	cJSON *nh = cJSON_Parse(getData(url));

	snprintf(url, sizeof url, "https://sessionserver.mojang.com/session/minecraft/profile/%s", uuid);
	cJSON *pf = cJSON_Parse(base64_decode(cJSON_GetObjectItem(cJSON_GetArrayItem(cJSON_GetObjectItem(cJSON_Parse(getData(url)), "properties"), 0), "value")->valuestring));

	printf("Done!\n");

	printf("\n");
	printf("Username: %s\n", username);
	printf("\n");
	printf("UUID: %s\n", uuid);
	printf("\n");
	printf("Username History:\n");
	cJSON_ArrayForEach(current_element, nh)
	{
		printf("- %s", cJSON_GetObjectItem(current_element, "name")->valuestring);
		if (cJSON_GetObjectItem(current_element, "changedToAt"))
		{
			printf(" (%s)\n", humanReadableTime((int)((cJSON_GetObjectItem(current_element, "changedToAt")->valuedouble) / 1000)));
		}
		else
		{
			printf("\n");
		}
	}
	printf("\n");
	if (cJSON_GetObjectItem(cJSON_GetObjectItem(cJSON_GetObjectItem(pf, "textures"), "SKIN"), "metadata"))
	{
		printf("Skin: %s (Slim)\n", cJSON_GetObjectItem(cJSON_GetObjectItem(cJSON_GetObjectItem(pf, "textures"), "SKIN"), "url")->valuestring);
	}
	else
	{
		printf("Skin: %s\n", cJSON_GetObjectItem(cJSON_GetObjectItem(cJSON_GetObjectItem(pf, "textures"), "SKIN"), "url")->valuestring);
	}
	printf("\n");
	if (cJSON_GetObjectItem(cJSON_GetObjectItem(pf, "textures"), "CAPE"))
	{
		printf("Cape: %s\n", cJSON_GetObjectItem(cJSON_GetObjectItem(cJSON_GetObjectItem(pf, "textures"), "CAPE"), "url")->valuestring);
	}
	else
	{
		printf("Cape: None\n");
	}

	return 0;
}