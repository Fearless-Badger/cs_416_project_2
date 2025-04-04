// define proxy for DEVSERVER, not prod(nginx)
//
// Route requests to proxy automatically
// For local testing, fastapi must have port 8000 exposed
//
// Basically, expose FastAPI ports in compose.yaml to develop locally with "npm run serve"

const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  devServer: {
    host: '0.0.0.0',
    port: 8080,
    proxy: {
      '^/api': {
        target: 'http://localhost:8000/',
        changeOrigin: true,
        pathRewrite: {
          '^/api': ''
        }
      }
    }
  },
  transpileDependencies: true,
  configureWebpack: {
    plugins: [],
  },
  pages: {
    index: {
      entry: 'src/main.js',
      title: 'Class Manager'
    }
  }
})
