{
    'name': 'Custom Login Page',
    'description': 'Customize the login page appearance',
    'category': 'Website',
    'version': '1.0',
    'author': 'Ocholi Joseph',
    'depends': ['web'],
    'data': [
        'views/custom_login_template.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            'custom_login/static/src/scss/custom_login.scss',
        ],
    },
}
