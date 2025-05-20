// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  compatibilityDate: '2024-11-01',
  devtools: { enabled: true },

  modules: [
    '@nuxt/eslint',
    '@nuxt/fonts',
    '@nuxt/icon',
    '@nuxt/image',
    '@nuxt/ui',
    '@sentry/nuxt/module'
  ],

  css: ['~/app/assets/css/main.css'],

  runtimeConfig: {
    public: {
      odesliAddress: 'https://api.song.link/v1-alpha.1'
    }
  },

  sentry: {
    sourceMapsUploadOptions: {
      org: 'lilylab',
      project: 'javascript-nuxt'
    }
  },

  sourcemap: {
    client: 'hidden'
  }
})