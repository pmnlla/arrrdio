<script setup lang="ts">
import { ref } from 'vue';
const items = ref(['Spotify', 'AppleMusic', 'YTMusic', 'Soundcloud'])
const value = ref('Spoify')

async function call() {
  const platform = ref('');
  const req = new Request("https://ntfy.sh/arrrdiotests", {
    method: "POST",
    body: platform.value,
    headers: {
        'Content-Type': 'text/plain',
      },
  });
  await $fetch(req);
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
