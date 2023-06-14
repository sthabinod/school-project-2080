
{
    "version":2,
    "builds": [{
        "src": "config/wsgi.py",
        "use": "@vercel/python",
        "config": { "maxLambdaSize": "15mb","runtime":"python:3.10" }
    },
    {
        "src": "build_files.sh",
        "use": "@vercel/static-build",
        "config": { "distDir": "statifiles_build" }
    }
    ],
    "routes": [
        {
            "src": "/static/(.*)",
            "dest": "/static/$1"
        },
        {
            "src": "/(.*)",
            "dest": "config/wsgi.py"
        }
    ]
}