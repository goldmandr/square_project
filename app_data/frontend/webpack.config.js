const path = require('path');
const MiniCssExtractPlugin = require('mini-css-extract-plugin');

module.exports = {
    resolve: {
        roots: [
            __dirname + '/src/'
        ],
        modules: ['node_modules'],
        extensions: ['.js', '.sass', '.scss', '.css']
    },
    entry: {
        libs: './src/_libs/libs_entry.js',
        auth: './src/auth/auth.js',
        app: './src/app/app.js',
        account: './src/account/account.js',
        square: './src/square/square.js'
    },
    output: {
        path: path.resolve(__dirname, '../static/'),
        filename: '[name]/bundles/[name].bundle.js'
    },
    module: {
        rules: [
            {
                test: /\.jsx?$/i,
                exclude: /node_modules/,
                use: [
                    {
                        loader: 'babel-loader'
                    }
                ]
            },
            {
                test: /\.s[ac]ss$/i,
                exclude: /node_modules/,
                use: [
                    MiniCssExtractPlugin.loader,
                    'css-loader',
                    'sass-loader'
                ]
            },
            {
                test: /\.css$/,
                use: [
                    MiniCssExtractPlugin.loader,
                    'css-loader'
                ]
            }
        ]
    },
    plugins: [
        new MiniCssExtractPlugin({
            filename: './[name]/bundles/[name].bundle.css'
        })
    ]
};
