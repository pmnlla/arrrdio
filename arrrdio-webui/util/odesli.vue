<script lang="ts" >

interface SongEntity {
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

async function callApi(path: string, parameters: Record<string, string>) {

    const conf = useRuntimeConfig();
    try {
        const request = await $fetch<any    >(path, {
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
  const songEntity: SongEntity | undefined = response?.entitiesByUniqueId
    ? Object.values(response.entitiesByUniqueId as Record<string, SongEntity>).find(
        (entity: SongEntity) => entity.type === "song"
      )
    : undefined;
  const songName = songEntity?.title || '' as string;
  console.log(songName);
  return songName;

}

export async function getAllAssociatedInfo(address: string) {
  const response = await callApi("links/", { url: address });
  const songEntity: SongEntity | undefined = response?.entitiesByUniqueId
    ? Object.values(response.entitiesByUniqueId as Record<string, SongEntity>).find(
        (entity: SongEntity) => entity.type === "song"
      )
    : undefined;
  const songName = songEntity?.title || '' as string;
  const songAuthor = songEntity?.artistName || '' as string;
  return [songName, songAuthor] as string[];

}

export async function getStreamLink(address: string) {
  const response = await callApi("links/", { url: address });
  console.warn(JSON.stringify(response));
  const songEntity: SongEntity | undefined = response?.entitiesByUniqueId?
    Object.values(response.entitiesByUniqueId as Record<string, SongEntity>).find(
      (entity: SongEntity) => entity.type === "song" && entity.platforms.includes("youtube")
    )
    : undefined;
    if (songEntity !== undefined) {
      const streamLink = response.linksByPlatform.youtube.url;
      console.warn(streamLink);
      return streamLink;  
    }
}
</script>