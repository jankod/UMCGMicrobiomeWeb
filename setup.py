from setuptools import setup

setup(
    name='UMCGMicrobiomeWeb',
    version='',
    packages=['app', 'app.migrations', 'app.templatetags', 'venv.Lib.site-packages.Bio',
              'venv.Lib.site-packages.Bio.GA', 'venv.Lib.site-packages.Bio.GA.Repair',
              'venv.Lib.site-packages.Bio.GA.Mutation', 'venv.Lib.site-packages.Bio.GA.Crossover',
              'venv.Lib.site-packages.Bio.GA.Selection', 'venv.Lib.site-packages.Bio.Geo',
              'venv.Lib.site-packages.Bio.HMM', 'venv.Lib.site-packages.Bio.NMR', 'venv.Lib.site-packages.Bio.PDB',
              'venv.Lib.site-packages.Bio.PDB.mmtf', 'venv.Lib.site-packages.Bio.PDB.QCPSuperimposer',
              'venv.Lib.site-packages.Bio.Affy', 'venv.Lib.site-packages.Bio.CAPS', 'venv.Lib.site-packages.Bio.Data',
              'venv.Lib.site-packages.Bio.FSSP', 'venv.Lib.site-packages.Bio.KEGG',
              'venv.Lib.site-packages.Bio.KEGG.Map', 'venv.Lib.site-packages.Bio.KEGG.Gene',
              'venv.Lib.site-packages.Bio.KEGG.KGML', 'venv.Lib.site-packages.Bio.KEGG.Enzyme',
              'venv.Lib.site-packages.Bio.KEGG.Compound', 'venv.Lib.site-packages.Bio.SCOP',
              'venv.Lib.site-packages.Bio.Wise', 'venv.Lib.site-packages.Bio._py3k', 'venv.Lib.site-packages.Bio.Align',
              'venv.Lib.site-packages.Bio.Align.Applications', 'venv.Lib.site-packages.Bio.Blast',
              'venv.Lib.site-packages.Bio.Nexus', 'venv.Lib.site-packages.Bio.Phylo',
              'venv.Lib.site-packages.Bio.Phylo.PAML', 'venv.Lib.site-packages.Bio.Phylo.Applications',
              'venv.Lib.site-packages.Bio.SeqIO', 'venv.Lib.site-packages.Bio.Emboss',
              'venv.Lib.site-packages.Bio.Entrez', 'venv.Lib.site-packages.Bio.ExPASy',
              'venv.Lib.site-packages.Bio.KDTree', 'venv.Lib.site-packages.Bio.motifs',
              'venv.Lib.site-packages.Bio.motifs.jaspar', 'venv.Lib.site-packages.Bio.motifs.applications',
              'venv.Lib.site-packages.Bio.PopGen', 'venv.Lib.site-packages.Bio.PopGen.GenePop',
              'venv.Lib.site-packages.Bio.TogoWS', 'venv.Lib.site-packages.Bio.AlignIO',
              'venv.Lib.site-packages.Bio.Cluster', 'venv.Lib.site-packages.Bio.Compass',
              'venv.Lib.site-packages.Bio.Crystal', 'venv.Lib.site-packages.Bio.GenBank',
              'venv.Lib.site-packages.Bio.Medline', 'venv.Lib.site-packages.Bio.Pathway',
              'venv.Lib.site-packages.Bio.Pathway.Rep', 'venv.Lib.site-packages.Bio.SubsMat',
              'venv.Lib.site-packages.Bio.UniGene', 'venv.Lib.site-packages.Bio.UniProt',
              'venv.Lib.site-packages.Bio.Alphabet', 'venv.Lib.site-packages.Bio.Graphics',
              'venv.Lib.site-packages.Bio.Graphics.GenomeDiagram', 'venv.Lib.site-packages.Bio.SearchIO',
              'venv.Lib.site-packages.Bio.SearchIO._model', 'venv.Lib.site-packages.Bio.SearchIO.BlastIO',
              'venv.Lib.site-packages.Bio.SearchIO.HmmerIO', 'venv.Lib.site-packages.Bio.SearchIO.ExonerateIO',
              'venv.Lib.site-packages.Bio.SearchIO.InterproscanIO', 'venv.Lib.site-packages.Bio.SeqUtils',
              'venv.Lib.site-packages.Bio.phenotype', 'venv.Lib.site-packages.Bio.SwissProt',
              'venv.Lib.site-packages.Bio.codonalign', 'venv.Lib.site-packages.Bio.Sequencing',
              'venv.Lib.site-packages.Bio.Sequencing.Applications', 'venv.Lib.site-packages.Bio.Statistics',
              'venv.Lib.site-packages.Bio.Application', 'venv.Lib.site-packages.Bio.Restriction',
              'venv.Lib.site-packages.Bio.NeuralNetwork', 'venv.Lib.site-packages.Bio.NeuralNetwork.Gene',
              'venv.Lib.site-packages.Bio.NeuralNetwork.BackPropagation', 'venv.Lib.site-packages.Bio.SVDSuperimposer',
              'venv.Lib.site-packages.pip', 'venv.Lib.site-packages.pip._vendor',
              'venv.Lib.site-packages.pip._vendor.idna', 'venv.Lib.site-packages.pip._vendor.pep517',
              'venv.Lib.site-packages.pip._vendor.pytoml', 'venv.Lib.site-packages.pip._vendor.certifi',
              'venv.Lib.site-packages.pip._vendor.chardet', 'venv.Lib.site-packages.pip._vendor.chardet.cli',
              'venv.Lib.site-packages.pip._vendor.distlib', 'venv.Lib.site-packages.pip._vendor.distlib._backport',
              'venv.Lib.site-packages.pip._vendor.msgpack', 'venv.Lib.site-packages.pip._vendor.urllib3',
              'venv.Lib.site-packages.pip._vendor.urllib3.util', 'venv.Lib.site-packages.pip._vendor.urllib3.contrib',
              'venv.Lib.site-packages.pip._vendor.urllib3.contrib._securetransport',
              'venv.Lib.site-packages.pip._vendor.urllib3.packages',
              'venv.Lib.site-packages.pip._vendor.urllib3.packages.backports',
              'venv.Lib.site-packages.pip._vendor.urllib3.packages.ssl_match_hostname',
              'venv.Lib.site-packages.pip._vendor.colorama', 'venv.Lib.site-packages.pip._vendor.html5lib',
              'venv.Lib.site-packages.pip._vendor.html5lib._trie',
              'venv.Lib.site-packages.pip._vendor.html5lib.filters',
              'venv.Lib.site-packages.pip._vendor.html5lib.treewalkers',
              'venv.Lib.site-packages.pip._vendor.html5lib.treeadapters',
              'venv.Lib.site-packages.pip._vendor.html5lib.treebuilders', 'venv.Lib.site-packages.pip._vendor.lockfile',
              'venv.Lib.site-packages.pip._vendor.progress', 'venv.Lib.site-packages.pip._vendor.requests',
              'venv.Lib.site-packages.pip._vendor.packaging', 'venv.Lib.site-packages.pip._vendor.cachecontrol',
              'venv.Lib.site-packages.pip._vendor.cachecontrol.caches',
              'venv.Lib.site-packages.pip._vendor.webencodings', 'venv.Lib.site-packages.pip._vendor.pkg_resources',
              'venv.Lib.site-packages.pip._internal', 'venv.Lib.site-packages.pip._internal.cli',
              'venv.Lib.site-packages.pip._internal.req', 'venv.Lib.site-packages.pip._internal.vcs',
              'venv.Lib.site-packages.pip._internal.utils', 'venv.Lib.site-packages.pip._internal.models',
              'venv.Lib.site-packages.pip._internal.commands', 'venv.Lib.site-packages.pip._internal.operations',
              'venv.Lib.site-packages.biom', 'venv.Lib.site-packages.biom.cli', 'venv.Lib.site-packages.biom.tests',
              'venv.Lib.site-packages.biom.tests.test_cli', 'venv.Lib.site-packages.biom.tests.test_data',
              'venv.Lib.site-packages.h5py', 'venv.Lib.site-packages.h5py._hl', 'venv.Lib.site-packages.h5py.tests',
              'venv.Lib.site-packages.h5py.tests.hl', 'venv.Lib.site-packages.h5py.tests.old',
              'venv.Lib.site-packages.past', 'venv.Lib.site-packages.past.tests', 'venv.Lib.site-packages.past.types',
              'venv.Lib.site-packages.past.utils', 'venv.Lib.site-packages.past.builtins',
              'venv.Lib.site-packages.past.translation', 'venv.Lib.site-packages.pytz', 'venv.Lib.site-packages.yaml',
              'venv.Lib.site-packages.click', 'venv.Lib.site-packages.numpy', 'venv.Lib.site-packages.numpy.ma',
              'venv.Lib.site-packages.numpy.ma.tests', 'venv.Lib.site-packages.numpy.doc',
              'venv.Lib.site-packages.numpy.fft', 'venv.Lib.site-packages.numpy.fft.tests',
              'venv.Lib.site-packages.numpy.lib', 'venv.Lib.site-packages.numpy.lib.tests',
              'venv.Lib.site-packages.numpy.core', 'venv.Lib.site-packages.numpy.core.tests',
              'venv.Lib.site-packages.numpy.f2py', 'venv.Lib.site-packages.numpy.f2py.tests',
              'venv.Lib.site-packages.numpy.tests', 'venv.Lib.site-packages.numpy.compat',
              'venv.Lib.site-packages.numpy.compat.tests', 'venv.Lib.site-packages.numpy.linalg',
              'venv.Lib.site-packages.numpy.linalg.tests', 'venv.Lib.site-packages.numpy.random',
              'venv.Lib.site-packages.numpy.random.tests', 'venv.Lib.site-packages.numpy.testing',
              'venv.Lib.site-packages.numpy.testing.tests', 'venv.Lib.site-packages.numpy.testing._private',
              'venv.Lib.site-packages.numpy.distutils', 'venv.Lib.site-packages.numpy.distutils.tests',
              'venv.Lib.site-packages.numpy.distutils.command', 'venv.Lib.site-packages.numpy.distutils.fcompiler',
              'venv.Lib.site-packages.numpy.matrixlib', 'venv.Lib.site-packages.numpy.matrixlib.tests',
              'venv.Lib.site-packages.numpy.polynomial', 'venv.Lib.site-packages.numpy.polynomial.tests',
              'venv.Lib.site-packages.scipy', 'venv.Lib.site-packages.scipy.io', 'venv.Lib.site-packages.scipy.io.arff',
              'venv.Lib.site-packages.scipy.io.arff.tests', 'venv.Lib.site-packages.scipy.io.tests',
              'venv.Lib.site-packages.scipy.io.matlab', 'venv.Lib.site-packages.scipy.io.matlab.tests',
              'venv.Lib.site-packages.scipy.io.harwell_boeing', 'venv.Lib.site-packages.scipy.io.harwell_boeing.tests',
              'venv.Lib.site-packages.scipy.odr', 'venv.Lib.site-packages.scipy.odr.tests',
              'venv.Lib.site-packages.scipy._lib', 'venv.Lib.site-packages.scipy._lib.tests',
              'venv.Lib.site-packages.scipy.misc', 'venv.Lib.site-packages.scipy.misc.tests',
              'venv.Lib.site-packages.scipy.stats', 'venv.Lib.site-packages.scipy.stats.tests',
              'venv.Lib.site-packages.scipy.linalg', 'venv.Lib.site-packages.scipy.linalg.tests',
              'venv.Lib.site-packages.scipy.signal', 'venv.Lib.site-packages.scipy.signal.tests',
              'venv.Lib.site-packages.scipy.signal.windows', 'venv.Lib.site-packages.scipy.sparse',
              'venv.Lib.site-packages.scipy.sparse.tests', 'venv.Lib.site-packages.scipy.sparse.linalg',
              'venv.Lib.site-packages.scipy.sparse.linalg.eigen',
              'venv.Lib.site-packages.scipy.sparse.linalg.eigen.arpack',
              'venv.Lib.site-packages.scipy.sparse.linalg.eigen.arpack.tests',
              'venv.Lib.site-packages.scipy.sparse.linalg.eigen.lobpcg',
              'venv.Lib.site-packages.scipy.sparse.linalg.eigen.lobpcg.tests',
              'venv.Lib.site-packages.scipy.sparse.linalg.tests', 'venv.Lib.site-packages.scipy.sparse.linalg.dsolve',
              'venv.Lib.site-packages.scipy.sparse.linalg.dsolve.tests',
              'venv.Lib.site-packages.scipy.sparse.linalg.isolve',
              'venv.Lib.site-packages.scipy.sparse.linalg.isolve.tests', 'venv.Lib.site-packages.scipy.sparse.csgraph',
              'venv.Lib.site-packages.scipy.sparse.csgraph.tests', 'venv.Lib.site-packages.scipy.cluster',
              'venv.Lib.site-packages.scipy.cluster.tests', 'venv.Lib.site-packages.scipy.fftpack',
              'venv.Lib.site-packages.scipy.fftpack.tests', 'venv.Lib.site-packages.scipy.ndimage',
              'venv.Lib.site-packages.scipy.ndimage.tests', 'venv.Lib.site-packages.scipy.spatial',
              'venv.Lib.site-packages.scipy.spatial.tests', 'venv.Lib.site-packages.scipy.special',
              'venv.Lib.site-packages.scipy.special.tests', 'venv.Lib.site-packages.scipy.special._precompute',
              'venv.Lib.site-packages.scipy.optimize', 'venv.Lib.site-packages.scipy.optimize._lsq',
              'venv.Lib.site-packages.scipy.optimize.tests', 'venv.Lib.site-packages.scipy.optimize._trlib',
              'venv.Lib.site-packages.scipy.optimize._trustregion_constr',
              'venv.Lib.site-packages.scipy.optimize._trustregion_constr.tests',
              'venv.Lib.site-packages.scipy.constants', 'venv.Lib.site-packages.scipy.constants.tests',
              'venv.Lib.site-packages.scipy.integrate', 'venv.Lib.site-packages.scipy.integrate._ivp',
              'venv.Lib.site-packages.scipy.integrate.tests', 'venv.Lib.site-packages.scipy.interpolate',
              'venv.Lib.site-packages.scipy.interpolate.tests', 'venv.Lib.site-packages.scipy._build_utils',
              'venv.Lib.site-packages.BioSQL', 'venv.Lib.site-packages.django', 'venv.Lib.site-packages.django.db',
              'venv.Lib.site-packages.django.db.models', 'venv.Lib.site-packages.django.db.models.sql',
              'venv.Lib.site-packages.django.db.models.fields', 'venv.Lib.site-packages.django.db.models.functions',
              'venv.Lib.site-packages.django.db.backends', 'venv.Lib.site-packages.django.db.backends.base',
              'venv.Lib.site-packages.django.db.backends.dummy', 'venv.Lib.site-packages.django.db.backends.mysql',
              'venv.Lib.site-packages.django.db.backends.oracle', 'venv.Lib.site-packages.django.db.backends.sqlite3',
              'venv.Lib.site-packages.django.db.backends.postgresql',
              'venv.Lib.site-packages.django.db.backends.postgresql_psycopg2',
              'venv.Lib.site-packages.django.db.migrations', 'venv.Lib.site-packages.django.db.migrations.operations',
              'venv.Lib.site-packages.django.apps', 'venv.Lib.site-packages.django.conf',
              'venv.Lib.site-packages.django.conf.urls', 'venv.Lib.site-packages.django.conf.locale',
              'venv.Lib.site-packages.django.conf.locale.ar', 'venv.Lib.site-packages.django.conf.locale.az',
              'venv.Lib.site-packages.django.conf.locale.bg', 'venv.Lib.site-packages.django.conf.locale.bn',
              'venv.Lib.site-packages.django.conf.locale.bs', 'venv.Lib.site-packages.django.conf.locale.ca',
              'venv.Lib.site-packages.django.conf.locale.cs', 'venv.Lib.site-packages.django.conf.locale.cy',
              'venv.Lib.site-packages.django.conf.locale.da', 'venv.Lib.site-packages.django.conf.locale.de',
              'venv.Lib.site-packages.django.conf.locale.el', 'venv.Lib.site-packages.django.conf.locale.en',
              'venv.Lib.site-packages.django.conf.locale.eo', 'venv.Lib.site-packages.django.conf.locale.es',
              'venv.Lib.site-packages.django.conf.locale.et', 'venv.Lib.site-packages.django.conf.locale.eu',
              'venv.Lib.site-packages.django.conf.locale.fa', 'venv.Lib.site-packages.django.conf.locale.fi',
              'venv.Lib.site-packages.django.conf.locale.fr', 'venv.Lib.site-packages.django.conf.locale.fy',
              'venv.Lib.site-packages.django.conf.locale.ga', 'venv.Lib.site-packages.django.conf.locale.gd',
              'venv.Lib.site-packages.django.conf.locale.gl', 'venv.Lib.site-packages.django.conf.locale.he',
              'venv.Lib.site-packages.django.conf.locale.hi', 'venv.Lib.site-packages.django.conf.locale.hr',
              'venv.Lib.site-packages.django.conf.locale.hu', 'venv.Lib.site-packages.django.conf.locale.id',
              'venv.Lib.site-packages.django.conf.locale.is', 'venv.Lib.site-packages.django.conf.locale.it',
              'venv.Lib.site-packages.django.conf.locale.ja', 'venv.Lib.site-packages.django.conf.locale.ka',
              'venv.Lib.site-packages.django.conf.locale.km', 'venv.Lib.site-packages.django.conf.locale.kn',
              'venv.Lib.site-packages.django.conf.locale.ko', 'venv.Lib.site-packages.django.conf.locale.lt',
              'venv.Lib.site-packages.django.conf.locale.lv', 'venv.Lib.site-packages.django.conf.locale.mk',
              'venv.Lib.site-packages.django.conf.locale.ml', 'venv.Lib.site-packages.django.conf.locale.mn',
              'venv.Lib.site-packages.django.conf.locale.nb', 'venv.Lib.site-packages.django.conf.locale.nl',
              'venv.Lib.site-packages.django.conf.locale.nn', 'venv.Lib.site-packages.django.conf.locale.pl',
              'venv.Lib.site-packages.django.conf.locale.pt', 'venv.Lib.site-packages.django.conf.locale.ro',
              'venv.Lib.site-packages.django.conf.locale.ru', 'venv.Lib.site-packages.django.conf.locale.sk',
              'venv.Lib.site-packages.django.conf.locale.sl', 'venv.Lib.site-packages.django.conf.locale.sq',
              'venv.Lib.site-packages.django.conf.locale.sr', 'venv.Lib.site-packages.django.conf.locale.sv',
              'venv.Lib.site-packages.django.conf.locale.ta', 'venv.Lib.site-packages.django.conf.locale.te',
              'venv.Lib.site-packages.django.conf.locale.th', 'venv.Lib.site-packages.django.conf.locale.tr',
              'venv.Lib.site-packages.django.conf.locale.uk', 'venv.Lib.site-packages.django.conf.locale.vi',
              'venv.Lib.site-packages.django.conf.locale.de_CH', 'venv.Lib.site-packages.django.conf.locale.en_AU',
              'venv.Lib.site-packages.django.conf.locale.en_GB', 'venv.Lib.site-packages.django.conf.locale.es_AR',
              'venv.Lib.site-packages.django.conf.locale.es_CO', 'venv.Lib.site-packages.django.conf.locale.es_MX',
              'venv.Lib.site-packages.django.conf.locale.es_NI', 'venv.Lib.site-packages.django.conf.locale.es_PR',
              'venv.Lib.site-packages.django.conf.locale.pt_BR', 'venv.Lib.site-packages.django.conf.locale.sr_Latn',
              'venv.Lib.site-packages.django.conf.locale.zh_Hans', 'venv.Lib.site-packages.django.conf.locale.zh_Hant',
              'venv.Lib.site-packages.django.core', 'venv.Lib.site-packages.django.core.mail',
              'venv.Lib.site-packages.django.core.mail.backends', 'venv.Lib.site-packages.django.core.cache',
              'venv.Lib.site-packages.django.core.cache.backends', 'venv.Lib.site-packages.django.core.files',
              'venv.Lib.site-packages.django.core.checks', 'venv.Lib.site-packages.django.core.checks.security',
              'venv.Lib.site-packages.django.core.checks.compatibility', 'venv.Lib.site-packages.django.core.servers',
              'venv.Lib.site-packages.django.core.handlers', 'venv.Lib.site-packages.django.core.management',
              'venv.Lib.site-packages.django.core.serializers', 'venv.Lib.site-packages.django.http',
              'venv.Lib.site-packages.django.test', 'venv.Lib.site-packages.django.urls',
              'venv.Lib.site-packages.django.forms', 'venv.Lib.site-packages.django.utils',
              'venv.Lib.site-packages.django.utils.translation', 'venv.Lib.site-packages.django.views',
              'venv.Lib.site-packages.django.views.generic', 'venv.Lib.site-packages.django.views.decorators',
              'venv.Lib.site-packages.django.contrib', 'venv.Lib.site-packages.django.contrib.gis',
              'venv.Lib.site-packages.django.contrib.gis.db', 'venv.Lib.site-packages.django.contrib.gis.db.models',
              'venv.Lib.site-packages.django.contrib.gis.db.models.sql',
              'venv.Lib.site-packages.django.contrib.gis.db.backends',
              'venv.Lib.site-packages.django.contrib.gis.db.backends.base',
              'venv.Lib.site-packages.django.contrib.gis.db.backends.mysql',
              'venv.Lib.site-packages.django.contrib.gis.db.backends.oracle',
              'venv.Lib.site-packages.django.contrib.gis.db.backends.postgis',
              'venv.Lib.site-packages.django.contrib.gis.db.backends.spatialite',
              'venv.Lib.site-packages.django.contrib.gis.gdal', 'venv.Lib.site-packages.django.contrib.gis.gdal.raster',
              'venv.Lib.site-packages.django.contrib.gis.gdal.prototypes',
              'venv.Lib.site-packages.django.contrib.gis.geos',
              'venv.Lib.site-packages.django.contrib.gis.geos.prototypes',
              'venv.Lib.site-packages.django.contrib.gis.admin', 'venv.Lib.site-packages.django.contrib.gis.forms',
              'venv.Lib.site-packages.django.contrib.gis.utils', 'venv.Lib.site-packages.django.contrib.gis.geoip2',
              'venv.Lib.site-packages.django.contrib.gis.sitemaps',
              'venv.Lib.site-packages.django.contrib.gis.serializers', 'venv.Lib.site-packages.django.contrib.auth',
              'venv.Lib.site-packages.django.contrib.auth.handlers',
              'venv.Lib.site-packages.django.contrib.auth.management',
              'venv.Lib.site-packages.django.contrib.auth.migrations', 'venv.Lib.site-packages.django.contrib.admin',
              'venv.Lib.site-packages.django.contrib.admin.views',
              'venv.Lib.site-packages.django.contrib.admin.migrations',
              'venv.Lib.site-packages.django.contrib.admin.templatetags', 'venv.Lib.site-packages.django.contrib.sites',
              'venv.Lib.site-packages.django.contrib.sites.migrations',
              'venv.Lib.site-packages.django.contrib.humanize',
              'venv.Lib.site-packages.django.contrib.humanize.templatetags',
              'venv.Lib.site-packages.django.contrib.messages',
              'venv.Lib.site-packages.django.contrib.messages.storage',
              'venv.Lib.site-packages.django.contrib.postgres', 'venv.Lib.site-packages.django.contrib.postgres.forms',
              'venv.Lib.site-packages.django.contrib.postgres.fields',
              'venv.Lib.site-packages.django.contrib.postgres.aggregates',
              'venv.Lib.site-packages.django.contrib.sessions',
              'venv.Lib.site-packages.django.contrib.sessions.backends',
              'venv.Lib.site-packages.django.contrib.sessions.migrations',
              'venv.Lib.site-packages.django.contrib.sitemaps', 'venv.Lib.site-packages.django.contrib.admindocs',
              'venv.Lib.site-packages.django.contrib.flatpages',
              'venv.Lib.site-packages.django.contrib.flatpages.migrations',
              'venv.Lib.site-packages.django.contrib.flatpages.templatetags',
              'venv.Lib.site-packages.django.contrib.redirects',
              'venv.Lib.site-packages.django.contrib.redirects.migrations',
              'venv.Lib.site-packages.django.contrib.staticfiles',
              'venv.Lib.site-packages.django.contrib.staticfiles.templatetags',
              'venv.Lib.site-packages.django.contrib.syndication', 'venv.Lib.site-packages.django.contrib.contenttypes',
              'venv.Lib.site-packages.django.contrib.contenttypes.management',
              'venv.Lib.site-packages.django.contrib.contenttypes.migrations', 'venv.Lib.site-packages.django.dispatch',
              'venv.Lib.site-packages.django.template', 'venv.Lib.site-packages.django.template.loaders',
              'venv.Lib.site-packages.django.template.backends', 'venv.Lib.site-packages.django.middleware',
              'venv.Lib.site-packages.django.templatetags', 'venv.Lib.site-packages.future',
              'venv.Lib.site-packages.future.moves', 'venv.Lib.site-packages.future.moves.dbm',
              'venv.Lib.site-packages.future.moves.html', 'venv.Lib.site-packages.future.moves.http',
              'venv.Lib.site-packages.future.moves.test', 'venv.Lib.site-packages.future.moves.urllib',
              'venv.Lib.site-packages.future.moves.xmlrpc', 'venv.Lib.site-packages.future.moves.tkinter',
              'venv.Lib.site-packages.future.tests', 'venv.Lib.site-packages.future.types',
              'venv.Lib.site-packages.future.utils', 'venv.Lib.site-packages.future.builtins',
              'venv.Lib.site-packages.future.backports', 'venv.Lib.site-packages.future.backports.html',
              'venv.Lib.site-packages.future.backports.http', 'venv.Lib.site-packages.future.backports.test',
              'venv.Lib.site-packages.future.backports.email', 'venv.Lib.site-packages.future.backports.email.mime',
              'venv.Lib.site-packages.future.backports.urllib', 'venv.Lib.site-packages.future.backports.xmlrpc',
              'venv.Lib.site-packages.future.standard_library', 'venv.Lib.site-packages.pandas',
              'venv.Lib.site-packages.pandas.io', 'venv.Lib.site-packages.pandas.io.sas',
              'venv.Lib.site-packages.pandas.io.json', 'venv.Lib.site-packages.pandas.io.formats',
              'venv.Lib.site-packages.pandas.io.msgpack', 'venv.Lib.site-packages.pandas.io.clipboard',
              'venv.Lib.site-packages.pandas.api', 'venv.Lib.site-packages.pandas.api.types',
              'venv.Lib.site-packages.pandas.api.extensions', 'venv.Lib.site-packages.pandas.core',
              'venv.Lib.site-packages.pandas.core.util', 'venv.Lib.site-packages.pandas.core.tools',
              'venv.Lib.site-packages.pandas.core.arrays', 'venv.Lib.site-packages.pandas.core.dtypes',
              'venv.Lib.site-packages.pandas.core.sparse', 'venv.Lib.site-packages.pandas.core.groupby',
              'venv.Lib.site-packages.pandas.core.indexes', 'venv.Lib.site-packages.pandas.core.reshape',
              'venv.Lib.site-packages.pandas.core.computation', 'venv.Lib.site-packages.pandas.util',
              'venv.Lib.site-packages.pandas._libs', 'venv.Lib.site-packages.pandas._libs.tslibs',
              'venv.Lib.site-packages.pandas.tests', 'venv.Lib.site-packages.pandas.tests.io',
              'venv.Lib.site-packages.pandas.tests.io.sas', 'venv.Lib.site-packages.pandas.tests.io.json',
              'venv.Lib.site-packages.pandas.tests.io.parser', 'venv.Lib.site-packages.pandas.tests.io.formats',
              'venv.Lib.site-packages.pandas.tests.io.msgpack', 'venv.Lib.site-packages.pandas.tests.api',
              'venv.Lib.site-packages.pandas.tests.util', 'venv.Lib.site-packages.pandas.tests.frame',
              'venv.Lib.site-packages.pandas.tests.tools', 'venv.Lib.site-packages.pandas.tests.dtypes',
              'venv.Lib.site-packages.pandas.tests.scalar', 'venv.Lib.site-packages.pandas.tests.scalar.period',
              'venv.Lib.site-packages.pandas.tests.scalar.interval',
              'venv.Lib.site-packages.pandas.tests.scalar.timedelta',
              'venv.Lib.site-packages.pandas.tests.scalar.timestamp', 'venv.Lib.site-packages.pandas.tests.series',
              'venv.Lib.site-packages.pandas.tests.series.indexing', 'venv.Lib.site-packages.pandas.tests.sparse',
              'venv.Lib.site-packages.pandas.tests.sparse.frame', 'venv.Lib.site-packages.pandas.tests.sparse.series',
              'venv.Lib.site-packages.pandas.tests.tslibs', 'venv.Lib.site-packages.pandas.tests.generic',
              'venv.Lib.site-packages.pandas.tests.groupby', 'venv.Lib.site-packages.pandas.tests.groupby.aggregate',
              'venv.Lib.site-packages.pandas.tests.indexes', 'venv.Lib.site-packages.pandas.tests.indexes.period',
              'venv.Lib.site-packages.pandas.tests.indexes.interval',
              'venv.Lib.site-packages.pandas.tests.indexes.datetimes',
              'venv.Lib.site-packages.pandas.tests.indexes.timedeltas', 'venv.Lib.site-packages.pandas.tests.reshape',
              'venv.Lib.site-packages.pandas.tests.reshape.merge', 'venv.Lib.site-packages.pandas.tests.tseries',
              'venv.Lib.site-packages.pandas.tests.tseries.offsets', 'venv.Lib.site-packages.pandas.tests.indexing',
              'venv.Lib.site-packages.pandas.tests.indexing.interval', 'venv.Lib.site-packages.pandas.tests.plotting',
              'venv.Lib.site-packages.pandas.tests.extension', 'venv.Lib.site-packages.pandas.tests.extension.base',
              'venv.Lib.site-packages.pandas.tests.extension.json',
              'venv.Lib.site-packages.pandas.tests.extension.decimal',
              'venv.Lib.site-packages.pandas.tests.extension.category', 'venv.Lib.site-packages.pandas.tests.internals',
              'venv.Lib.site-packages.pandas.tests.categorical', 'venv.Lib.site-packages.pandas.tests.computation',
              'venv.Lib.site-packages.pandas.tools', 'venv.Lib.site-packages.pandas.types',
              'venv.Lib.site-packages.pandas.compat', 'venv.Lib.site-packages.pandas.compat.numpy',
              'venv.Lib.site-packages.pandas.errors', 'venv.Lib.site-packages.pandas.formats',
              'venv.Lib.site-packages.pandas.tseries', 'venv.Lib.site-packages.pandas.plotting',
              'venv.Lib.site-packages.pandas.computation', 'venv.Lib.site-packages.include',
              'venv.Lib.site-packages.include.base', 'venv.Lib.site-packages.include.files',
              'venv.Lib.site-packages.include.mount', 'venv.Lib.site-packages.include.encoded',
              'venv.Lib.site-packages.MySQLdb', 'venv.Lib.site-packages.MySQLdb.constants',
              'venv.Lib.site-packages.dateutil', 'venv.Lib.site-packages.dateutil.tz',
              'venv.Lib.site-packages.dateutil.parser', 'venv.Lib.site-packages.dateutil.zoneinfo',
              'venv.Lib.site-packages.httplib2', 'venv.Lib.site-packages.sqlparse',
              'venv.Lib.site-packages.sqlparse.engine', 'venv.Lib.site-packages.sqlparse.filters',
              'venv.Lib.site-packages.formtools', 'venv.Lib.site-packages.formtools.wizard',
              'venv.Lib.site-packages.formtools.wizard.storage', 'venv.Lib.site-packages.bootstrap4',
              'venv.Lib.site-packages.bootstrap4.templatetags', 'venv.Lib.site-packages.setuptools',
              'venv.Lib.site-packages.setuptools.extern', 'venv.Lib.site-packages.setuptools._vendor',
              'venv.Lib.site-packages.setuptools._vendor.packaging', 'venv.Lib.site-packages.setuptools.command',
              'venv.Lib.site-packages.libfuturize', 'venv.Lib.site-packages.libfuturize.fixes',
              'venv.Lib.site-packages.crispy_forms', 'venv.Lib.site-packages.crispy_forms.tests',
              'venv.Lib.site-packages.crispy_forms.templatetags', 'venv.Lib.site-packages.test_include',
              'venv.Lib.site-packages.debug_toolbar', 'venv.Lib.site-packages.debug_toolbar.panels',
              'venv.Lib.site-packages.debug_toolbar.panels.sql',
              'venv.Lib.site-packages.debug_toolbar.panels.templates',
              'venv.Lib.site-packages.debug_toolbar.management',
              'venv.Lib.site-packages.debug_toolbar.management.commands',
              'venv.Lib.site-packages.debug_toolbar.templatetags', 'venv.Lib.site-packages.libpasteurize',
              'venv.Lib.site-packages.libpasteurize.fixes', 'venv.Lib.site-packages.pkg_resources',
              'venv.Lib.site-packages.pkg_resources.extern', 'venv.Lib.site-packages.pkg_resources._vendor',
              'venv.Lib.site-packages.pkg_resources._vendor.packaging',
              'venv.Lib.site-packages.pip-10.0.1-py3.6.egg.pip',
              'venv.Lib.site-packages.pip-10.0.1-py3.6.egg.pip._vendor',
              'venv.Lib.site-packages.pip-10.0.1-py3.6.egg.pip._vendor.idna',
              'venv.Lib.site-packages.pip-10.0.1-py3.6.egg.pip._vendor.pytoml',
              'venv.Lib.site-packages.pip-10.0.1-py3.6.egg.pip._vendor.certifi',
              'venv.Lib.site-packages.pip-10.0.1-py3.6.egg.pip._vendor.chardet',
              'venv.Lib.site-packages.pip-10.0.1-py3.6.egg.pip._vendor.chardet.cli',
              'venv.Lib.site-packages.pip-10.0.1-py3.6.egg.pip._vendor.distlib',
              'venv.Lib.site-packages.pip-10.0.1-py3.6.egg.pip._vendor.distlib._backport',
              'venv.Lib.site-packages.pip-10.0.1-py3.6.egg.pip._vendor.msgpack',
              'venv.Lib.site-packages.pip-10.0.1-py3.6.egg.pip._vendor.urllib3',
              'venv.Lib.site-packages.pip-10.0.1-py3.6.egg.pip._vendor.urllib3.util',
              'venv.Lib.site-packages.pip-10.0.1-py3.6.egg.pip._vendor.urllib3.contrib',
              'venv.Lib.site-packages.pip-10.0.1-py3.6.egg.pip._vendor.urllib3.contrib._securetransport',
              'venv.Lib.site-packages.pip-10.0.1-py3.6.egg.pip._vendor.urllib3.packages',
              'venv.Lib.site-packages.pip-10.0.1-py3.6.egg.pip._vendor.urllib3.packages.backports',
              'venv.Lib.site-packages.pip-10.0.1-py3.6.egg.pip._vendor.urllib3.packages.ssl_match_hostname',
              'venv.Lib.site-packages.pip-10.0.1-py3.6.egg.pip._vendor.colorama',
              'venv.Lib.site-packages.pip-10.0.1-py3.6.egg.pip._vendor.html5lib',
              'venv.Lib.site-packages.pip-10.0.1-py3.6.egg.pip._vendor.html5lib._trie',
              'venv.Lib.site-packages.pip-10.0.1-py3.6.egg.pip._vendor.html5lib.filters',
              'venv.Lib.site-packages.pip-10.0.1-py3.6.egg.pip._vendor.html5lib.treewalkers',
              'venv.Lib.site-packages.pip-10.0.1-py3.6.egg.pip._vendor.html5lib.treeadapters',
              'venv.Lib.site-packages.pip-10.0.1-py3.6.egg.pip._vendor.html5lib.treebuilders',
              'venv.Lib.site-packages.pip-10.0.1-py3.6.egg.pip._vendor.lockfile',
              'venv.Lib.site-packages.pip-10.0.1-py3.6.egg.pip._vendor.progress',
              'venv.Lib.site-packages.pip-10.0.1-py3.6.egg.pip._vendor.requests',
              'venv.Lib.site-packages.pip-10.0.1-py3.6.egg.pip._vendor.packaging',
              'venv.Lib.site-packages.pip-10.0.1-py3.6.egg.pip._vendor.cachecontrol',
              'venv.Lib.site-packages.pip-10.0.1-py3.6.egg.pip._vendor.cachecontrol.caches',
              'venv.Lib.site-packages.pip-10.0.1-py3.6.egg.pip._vendor.webencodings',
              'venv.Lib.site-packages.pip-10.0.1-py3.6.egg.pip._vendor.pkg_resources',
              'venv.Lib.site-packages.pip-10.0.1-py3.6.egg.pip._internal',
              'venv.Lib.site-packages.pip-10.0.1-py3.6.egg.pip._internal.req',
              'venv.Lib.site-packages.pip-10.0.1-py3.6.egg.pip._internal.vcs',
              'venv.Lib.site-packages.pip-10.0.1-py3.6.egg.pip._internal.utils',
              'venv.Lib.site-packages.pip-10.0.1-py3.6.egg.pip._internal.models',
              'venv.Lib.site-packages.pip-10.0.1-py3.6.egg.pip._internal.commands',
              'venv.Lib.site-packages.pip-10.0.1-py3.6.egg.pip._internal.operations',
              'venv.Lib.site-packages.global_login_required', 'UMCGMicrobiomeWeb', 'UMCGMicrobiomeWeb.settings'],
    url='',
    license='',
    author='Janko Diminic',
    author_email='',
    description=''
)
