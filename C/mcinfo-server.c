#include <stdio.h>
#include <stdlib.h>
#include <curl/curl.h>
#include <string.h>
#include "cJSON/cJSON.h"

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
	char address[256];
	char url[512];

	printf("Address: ");
	scanf("%s", address) == 1;

	printf("Gathering some data...\n");

	snprintf(url, sizeof url, "https://api.mcsrvstat.us/2/%s", address);
	cJSON *info = cJSON_Parse(getData(url));

	printf("Done!\n");
	printf("\n");

	if (cJSON_IsTrue(cJSON_GetObjectItem(info, "online")))
	{
		printf("Address: %s\n", address);
		printf("\n");
		printf("MOTD: %s\n", cJSON_GetArrayItem(cJSON_GetObjectItem(cJSON_GetObjectItem(info, "motd"), "clean"), 0)->valuestring);
		printf("\n");
		printf("Players: ");
		if (cJSON_GetObjectItem(cJSON_GetObjectItem(info, "players"), "list"))
		{
			char players[32768];

			cJSON_ArrayForEach(current_element, cJSON_GetObjectItem(cJSON_GetObjectItem(info, "players"), "list"))
			{
				strcat(players, current_element->valuestring);
				strcat(players, ", ");
			}

			players[strlen(players) - 2] = '\0';

			printf("%s (%d/%d)\n", players, cJSON_GetObjectItem(cJSON_GetObjectItem(info, "players"), "online")->valueint, cJSON_GetObjectItem(cJSON_GetObjectItem(info, "players"), "max")->valueint);
		}
		else if (cJSON_GetObjectItem(cJSON_GetObjectItem(info, "players"), "online")->valueint)
		{
			printf("%d/%d\n", cJSON_GetObjectItem(cJSON_GetObjectItem(info, "players"), "online")->valueint, cJSON_GetObjectItem(cJSON_GetObjectItem(info, "players"), "max")->valueint);
		}
		else
		{
			printf("None\n");
		}
		printf("\n");
		printf("Version: %s\n", cJSON_GetObjectItem(info, "version")->valuestring);
		printf("\n");
		if (cJSON_GetObjectItem(info, "hostname"))
		{
			printf("Hostname: %s\n", cJSON_GetObjectItem(info, "hostname")->valuestring);
		}
		else
		{
			printf("Hostname: None\n");
		}
		printf("\n");
		if (cJSON_GetObjectItem(info, "software"))
		{
			printf("Software: %s\n", cJSON_GetObjectItem(info, "software")->valuestring);
		}
		else
		{
			printf("Software: None\n");
		}
		printf("\n");
		if (cJSON_GetObjectItem(info, "plugins"))
		{
			char plugins[32768];

			cJSON_ArrayForEach(current_element, cJSON_GetObjectItem(cJSON_GetObjectItem(info, "plugins"), "names"))
			{
				strcat(plugins, current_element->valuestring);
				strcat(plugins, ", ");
			}

			plugins[strlen(plugins) - 2] = '\0';

			printf("Plugins: %s\n", plugins);
		}
		else if (cJSON_GetObjectItem(info, "mods"))
		{
			char mods[32768];

			cJSON_ArrayForEach(current_element, cJSON_GetObjectItem(cJSON_GetObjectItem(info, "mods"), "names"))
			{
				strcat(mods, current_element->valuestring);
				strcat(mods, ", ");
			}

			mods[strlen(mods) - 2] = '\0';

			printf("Mods: %s\n", mods);
		} else {
			printf("Plugins/Mods: None\n");
		}
	}
	else
	{
		printf("Server Offline.\n");
	}

	return 0;
}