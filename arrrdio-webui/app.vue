<script setup lang="ts">
import { ref } from 'vue';
var songLink = ref('')
var ApiCall = ref('')
import { getAllAssociatedInfo, getOdesliLink, getSongName, getStreamLink, writeSongEntity } from "@/util/odesli.vue"

/// <reference types="../node_modules/.vue-global-types/vue_3.5_0_0_0.d.ts" />
import type { TrackInfo, CastEntity } from "@/util/castEntity.vue";
// im gonna be so fr i have no clue what that first line does, vscode just suggested it. sigma balls

const toast = useToast()

async function call() {

  const castEntity = await writeSongEntity(songLink.value);
  if (castEntity && castEntity._trackInfo) {
    showSongToast(castEntity._trackInfo.title, castEntity._trackInfo.artist);
  } else {
    console.log(castEntity?._trackInfo.title);
  }
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
