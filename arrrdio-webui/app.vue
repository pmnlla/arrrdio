<script setup lang="ts">
const items = ref(['Spotify', 'AppleMusic', 'YTMusic', 'Soundcloud'])
const value = ref('Spoify')
</script>

<template>
  <div class="flex flex-col items-center justify-center h-screen">
    <USelectMenu v-model="value" :items="items" class="w-48" />
    <br>
    <UFormField label="Link" description="We'll use this to queue up your song on the Arrrdio!">
      <UInput placeholder="Enter song link:" class="w-full" />
    </UFormField>
  </div>
</template>
