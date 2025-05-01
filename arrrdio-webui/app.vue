<script setup lang="ts">
import { ref } from 'vue';
const items = ref(['Spotify', 'AppleMusic', 'YTMusic', 'Soundcloud'])
var platform = ref('Spotify')
var songLink = ref('')

import { getOdesliLink } from "@/util/odesli.vue"

async function call() {
  const data = await getOdesliLink(songLink.value);
  console.log(JSON.stringify(data));

  const req_ntfy = new Request("https://ntfy.sh/arrrdiotests", {
    method: "POST",
    body: JSON.stringify(data),
    headers: {
        'Content-Type': 'text/plain',
      },
  });
  await $fetch(req_ntfy);
}
</script>

<template>
  <div class="flex flex-col items-center justify-center h-screen gap-6">
    <UFormField label="Platform" description="To ensure we get the correct information from your link!" class="w-96 flex items-center jutify-center">
    <USelectMenu v-model="platform" :items="items" class="w-48" />
    </UFormField>
    <UFormField label="Link" description="We'll use this to queue up your song on the Arrrdio!" class="w-96">
      <UInput v-model="songLink" placeholder="Enter song link:" class="w-full" />
    </UFormField>
    <UButton @click="call" loading-auto trailing-icon="i-lucide-arrow-right" size="md" label="Set Sail!" />
  </div>
</template>
