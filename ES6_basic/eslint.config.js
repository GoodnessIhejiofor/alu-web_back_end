import { ESLint } from 'eslint';

export default new ESLint({
  baseConfig: {
    env: {
      browser: true,
      es2021: true,
      node: true
    },
    extends: 'eslint:recommended',
    parserOptions: {
      ecmaVersion: 'latest',
      sourceType: 'module'
    },
    rules: {
      'eol-last': ['error', 'always'],
      // Add other rules you need here
    }
  }
});
