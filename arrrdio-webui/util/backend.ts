import { isJsxOpeningElement } from "typescript";
import type { CastEntity } from "./castEntity";

interface SongDataRequest {
    _entry: CastEntity
}

async function callApi(path: string, parameters: Record<string, string>, data: string) {

    const conf = useRuntimeConfig();
    try {
        const request = await $fetch<any>(path, {
            method: "POST",
            mode: 'no-cors', // in theory, you should never do this. but we don't actually care for the output of the request - at least yet.
            baseURL: conf.public.backendAddress as string,
            body: data,
            params: parameters,
            timeout: 15000
        });
        return request;
    } catch (err) {
        alert(err);
    }

}

export async function pushSong(entity: CastEntity) {
  const data: SongDataRequest = {
    _entry: entity
  }
  console.log(JSON.stringify(data));
  const response = await callApi("interface/request", {}, JSON.stringify(data));
  return response;
}
