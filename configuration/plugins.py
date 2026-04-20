PLUGINS = [
	"netbox_inventory",
	"netbox_branching"
]

from netbox_branching.utilities import DynamicSchemaDict

DATABASES = DynamicSchemaDict({
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'netbox',                 # Database name
        'USER': 'netbox',                 # PostgreSQL username
        'PASSWORD': 'J5brHrAXFLQSif0K',       # PostgreSQL password
        'HOST': 'postgres',               # Database server
        'PORT': '',                       # Database port (leave blank for default)
        'CONN_MAX_AGE': 300,              # Max database connection age
    }
})

DATABASE_ROUTERS = [
    'netbox_branching.database.BranchAwareRouter',
]
