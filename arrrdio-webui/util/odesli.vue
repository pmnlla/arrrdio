<script lang="ts" >

async function callApi(path: string, parameters: Record<string, string>) {

    const conf = useRuntimeConfig();
    try {
        const request = await $fetch<any    >(path, {
            baseURL: conf.public.odesliAddress as string,
            params: parameters,
            timeout: 1000
        });
        alert(JSON.stringify(request));
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

export async function getAMLink(address: string) {
  const response = await callApi("links/", { url: address });
  const entry = response?.entitiesByUniqueId.filter((e: string) => e.startsWith("ITUNES_SONG")) || '';
  console.log(entry);
  return entry;
}
</script>