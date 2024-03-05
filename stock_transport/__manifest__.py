{
    "name" : "Transport Management System",
    "version" : "17.0.1.0.0",
    'depends' : ['stock_picking_batch', 'fleet'],
    'data': [
        'views/fleet_vehicle_model_views.xml',
        'views/stock_picking_batch_views.xml',
        'views/stock_picking_views.xml',
    ],
    'installable': True,
    'license': 'LGPL-3',
}