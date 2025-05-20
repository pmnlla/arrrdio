import * as Sentry from "@sentry/nuxt";
 
Sentry.init({
  dsn: "https://c34f1a13c76a1756f994adc57d7db186@o4509330514509824.ingest.us.sentry.io/4509330548457472",

  // We recommend adjusting this value in production, or using tracesSampler
  // for finer control
  tracesSampleRate: 1.0,
  
  // Setting this option to true will print useful information to the console while you're setting up Sentry.
  debug: false,
});
