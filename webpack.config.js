const createWebpackConfig = require('@dabapps/create-webpack-config');

module.exports = createWebpackConfig({
  input: './static/src/ts/index.tsx',
  outDir: './static/build/js',
  tsconfig: './tsconfig.dist.json',
  rawFileExtensions: ['txt'],
  env: {
    NODE_ENV: 'production'
  }
});
