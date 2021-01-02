make:
	gcc mcinfo-player.c base64/base64.c base64/base64.h cJSON/cJSON.h cJSON/cJSON.c -lcurl -O3 -o mcinfo-player
	gcc mcinfo-server.c cJSON/cJSON.h cJSON/cJSON.c -lcurl -O3 -o mcinfo-server

clean:
	rm -f mcinfo-player mcinfo-server