let Encore = require('@symfony/webpack-encore');
let main_dir = './app/static';

Encore
    // directory where compiled assets will be stored
    .setOutputPath('app/static/build/')
    // public path used by the web server to access the output path
    .setPublicPath('/static/build/')
    // only needed for CDN's or sub-directory deploy
    //.setManifestKeyPrefix('build/')

    /*
     * ENTRY CONFIG
     *
     * Add 1 entry for each "page" of your app
     * (including one that's included on every page - e.g. "app")
     *
     * Each entry will result in one JavaScript file (e.g. base.js)
     * and one CSS file (e.g. app.css) if you JavaScript imports CSS.
     */
    .addEntry('base', main_dir + '/js/base.js')



  //  .addEntry('fonts/font-awesome', './node_modules/font-awesome/css/fontawesome.css')
//    .addEntry('fonts/fontawesome-webfont.eot', './node_modules/font-awesome/fonts/fontawesome-webfont.eot')

//    .addStyleEntry('header', main_dir + '/css/header.scss')

    // will require an extra script tag for runtime.js
    // but, you probably want this, unless you're building a single-page app
    .enableSingleRuntimeChunk()

    .cleanupOutputBeforeBuild()
    .enableSourceMaps(!Encore.isProduction())
    // enables hashed filenames (e.g. app.abc123.css)
    .enableVersioning(Encore.isProduction())

    .enableSassLoader()

    .autoProvidejQuery()
;

module.exports = Encore.getWebpackConfig();