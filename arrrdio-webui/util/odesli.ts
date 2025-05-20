/// <reference types="../node_modules/.vue-global-types/vue_3.5_0_0_0.d.ts" />
import type { TrackInfo, CastEntity } from "~/util/castEntity";
// im gonna be so fr i have no clue what that first line does, vscode just suggested it. sigma balls

interface SongEntity_NoLink {
  id: string;
  type: string;
  title: string;
  artistName: string;
  thumbnailUrl: string;
  thumbnailWidth: number;
  thumbnailHeight: number;
  apiProvider: string;
  platforms: string[];
}

interface SongEntity {
  id: string;
  type: string;
  title: string;
  artistName: string;
  thumbnailUrl: string;
  thumbnailWidth: number;
  thumbnailHeight: number;
  apiProvider: string;
  link: string;
  platforms: string[];
}


async function callApi(path: string, parameters: Record<string, string>) {

    const conf = useRuntimeConfig();
    try {
        const request = await $fetch<any>(path, {
            baseURL: conf.public.odesliAddress as string,
            params: parameters,
            timeout: 15000
        });
        return request;
    } catch (err) {
        alert(err);
    }

}

export async function getOdesliLink(address: string) {
  const response = await callApi("links/", { url: address });
  const pageUrl = response?.pageUrl || '';
  console.log(pageUrl);
  return pageUrl;
}

export async function getSongName(address: string) {
  const response = await callApi("links/", { url: address });
  const songEntity: SongEntity_NoLink | undefined = response?.entitiesByUniqueId
    ? Object.values(response.entitiesByUniqueId as Record<string, SongEntity_NoLink>).find(
        (entity: SongEntity_NoLink) => entity.type === "song"
      )
    : undefined;
  const songName = songEntity?.title || '' as string;
  console.log(songName);
  return songName;

}

export async function getAllAssociatedInfo(address: string) {
  const response = await callApi("links/", { url: address });
  const songEntity: SongEntity_NoLink | undefined = response?.entitiesByUniqueId
    ? Object.values(response.entitiesByUniqueId as Record<string, SongEntity_NoLink>).find(
        (entity: SongEntity_NoLink) => entity.type === "song"
      )
    : undefined;
  const songName = songEntity?.title || '' as string;
  const songAuthor = songEntity?.artistName || '' as string;
  return [songName, songAuthor] as string[];

}

export async function getStreamLink(address: string) {
  const response = await callApi("links/", { url: address });
  console.warn(JSON.stringify(response));
  const songEntity: SongEntity_NoLink | undefined = response?.entitiesByUniqueId?
    Object.values(response.entitiesByUniqueId as Record<string, SongEntity_NoLink>).find(
      (entity: SongEntity_NoLink) => entity.type === "song" && entity.platforms.includes("youtube")
    )
    : undefined;
    if (songEntity !== undefined) {
      const streamLink = response.linksByPlatform.youtube.url;
      console.warn(streamLink);
      return streamLink;  
    }
  }
  export async function writeSongEntity(address: string) {
  const response = await callApi("links/", { url: address });
  const songEntity: SongEntity_NoLink | undefined = response?.entitiesByUniqueId
    ? Object.values(response.entitiesByUniqueId as Record<string, SongEntity_NoLink>).find(
        (entity: SongEntity_NoLink) => entity.type === "song"
      )
    : undefined;
  try {
    if (songEntity) {
      const finalEntity: SongEntity = {
        ...songEntity,
        link: response?.LinksByPlatform?.youtubeMusic?.url || ''
      } as SongEntity;

      const trackInfoEntity: TrackInfo =  {
        title: finalEntity.title,
        album: "null - unsupported by odesli",
        artist: finalEntity.artistName,
        thumbnailUrl: finalEntity.thumbnailUrl
      }

      const link = finalEntity.link.substring(34, 46); // exclusive, inclusive -- youtube video IDs are always 12 characters long.

      const finalCastEntity: CastEntity = {
        _trackInfo: trackInfoEntity,
        address: link,
        odesliEntityId: response?.entityUniqueId
      }

      return finalCastEntity;
    } else {
      throw new Error("No song entity found");
    }
  } catch (err) {
    console.error(err);
    return null; // or throw err;
  }
} 