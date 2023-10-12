{
    'name': 'Website Session',
    "version": "16.0.1.0.0",
    'description': 'Website session to show the form page,menu addition',
    "author": 'Cybrosys',
    'license': 'LGPL-3',
    'category': 'Website',
    "depends": [
        "base",
        'website',
    ],
    "data": [
        'data/website_menu_data.xml',
        "views/website_partner_view.xml",

    ],
    # 'assets': {
    #     # 'web.assets_frontend': [
    #     #     'website_grid_view/static/src/css/website_display_type.css',]
    #         # 'website_grid_view/static/src/js/website_display_type.js'],
    #
    # },
    "auto-install": True,
    "application": True,
    "installable": True,

}
