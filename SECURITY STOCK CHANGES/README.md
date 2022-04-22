--- MODIFICATION
product.py
    real path='addons\stock\models\product.py'
    - Ajout des champs:
            -supply_delay
            -annual_demand
            -security_stock (computed)
    - Fonction _compute_security_stock qui calcule le stock de sécurité autoamtiquement et dépend de supply delay & annual demand


product_views.xml
    real path = 'addons\stock\views\product_views.xml'
    - Ajout des champs respectifs à l'onget stock de la vue des produit