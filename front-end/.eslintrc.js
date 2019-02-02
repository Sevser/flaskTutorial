// https://eslint.org/docs/user-guide/configuring
const path = require('path');

module.exports = {
	root: true,
	parserOptions: {
		parser: 'babel-eslint'
	},
	env: {
		browser: true,
	},
	// https://github.com/vuejs/eslint-plugin-vue#priority-a-essential-error-prevention
	// consider switching to `plugin:vue/strongly-recommended` or `plugin:vue/recommended` for stricter rules.
	extends: ['plugin:vue/essential', 'airbnb-base'],
	// required to lint *.vue files
	plugins: [
		'vue'
	],
	settings: {
		'import/resolver': {
			alias: {
				extensions: ['.js', '.vue', '.json'],
				map: [
					['@', path.resolve(__dirname, './src')],
				],
			}
		}
	},
	// add your custom rules here
	rules: {
		"no-console": "off",
		// don't require .vue extension when importing
		'import/extensions': ['error', 'always', {
			"js": "never",
			"vue": "never"
		}],
		"eqeqeq": "warn",
		"quotes": ["error", "single"],
		"quote-props": ["error", "consistent"],
		// disallow reassignment of function parameters
		// disallow parameter object manipulation except for specific exclusions
		'no-param-reassign': ['error', {
			props: true,
			ignorePropertyModificationsFor: [
				'state', // for vuex state
				'acc', // for reduce accumulators
				'e' // for e.returnvalue
			]
		}],
		// allow optionalDependencies
		'import/no-extraneous-dependencies': ['error', {
			optionalDependencies: ['test/unit/index.js']
		}],
		// allow debugger during development
		'no-debugger': process.env.NODE_ENV === 'production' ? 'error' : 'off',
		"eslint linebreak-style": [0, "error", "windows"],
		"linebreak-style": 0,
		// "no-param-reassign": [2, {"props": false}],
		"no-underscore-dangle": "off",
		'import/no-extraneous-dependencies': ['error', {
			optionalDependencies: ['test/unit/index.js']
		}],
		'max-len': ['error', {'code': 121, 'ignoreTemplateLiterals': true, 'ignoreStrings': true, 'ignoreUrls': true}]
	}
}