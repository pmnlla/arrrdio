<script setup lang="ts">
import { ref } from 'vue';
var songLink = ref('')

import { getAllAssociatedInfo, getOdesliLink, getSongName, getStreamLink } from "@/util/odesli.vue"

const toast = useToast()

async function call() {

  const data = await getAllAssociatedInfo(songLink.value);
  /*
  const req_ntfy = new Request("https://ntfy.sh/arrrdiotests", {
    method: "POST",
    body: data,
    headers: {
        'Content-Type': 'text/plain',
      },
  });
  await $fetch(req_ntfy);*/

  showSongToast(data[0] as string, data[1] as string);

}

function showSongToast(name: string, author: string) {
  console.log(name);
  toast.add({
    title: `Added ${name}!`,
    description: `${name} by ${author} is in the queue.`
  })
}

</script>

<template>
  <UApp>
  <div class="flex flex-col items-center justify-center h-screen gap-6">
    <UFormField label="Link" description="We'll use this to queue up your song on the Arrrdio!" class="w-96">
      <UInput v-model="songLink" placeholder="Enter song link:" class="w-full" />
    </UFormField>
    <UButton @click="call" loading-auto trailing-icon="i-lucide-arrow-right" size="md" label="Set Sail!" />
  </div>
</UApp>
</template>
