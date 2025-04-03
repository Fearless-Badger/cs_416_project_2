// define proxy for DEVSERVER, not prod(nginx)
//
// Route requests to proxy automatically
// For local testing, fastapi must have port 8000 exposed
//
// Basically, expose FastAPI ports in compose.yaml to develop locally with "npm run serve"

const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  devServer: {
    proxy: "http://fastapi_app:8000"
  },
  transpileDependencies: true
})
