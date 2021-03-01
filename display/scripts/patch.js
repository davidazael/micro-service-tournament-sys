const fs = require('fs')
const path = require('path')

const loadTrackingPath = path.resolve(
  __dirname,
  '../node_modules/@vue/apollo-composable/dist/util/loadingTracking.js'
)

fs.writeFileSync(
  loadTrackingPath,
  fs.readFileSync(loadTrackingPath, 'utf8').replace(/\.\$root/m, '.root')
)

const useQueryPath = path.resolve(
  __dirname,
  '../node_modules/@vue/apollo-composable/dist/useQuery.js'
)

const vueApolloComposablePath = path.resolve(
  __dirname,
  '../node_modules/@vue/apollo-composable/dist/vue-apollo-composable.js'
)

fs.writeFileSync(
  useQueryPath,
  fs.readFileSync(useQueryPath, 'utf8').replace(/^onServerPrefetch, /mu, '')
)

fs.writeFileSync(
  useQueryPath,
  fs
    .readFileSync(useQueryPath, 'utf8')
    .replace(/onServerPrefetch === null.*?\}\);/msu, '')
)

fs.writeFileSync(
  vueApolloComposablePath,
  fs
    .readFileSync(vueApolloComposablePath, 'utf8')
    .replace(/vue_demi_5.onServerPrefetch === null.*?\}\);/msu, '')
)
