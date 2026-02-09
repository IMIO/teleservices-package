if "passerelle_imio_apims_baec" not in INSTALLED_APPS:
    INSTALLED_APPS += ("passerelle_imio_apims_baec",)
    TENANT_APPS += ("passerelle_imio_apims_baec",)

if 'passerelle_imio_apims_casier_judiciaire' not in INSTALLED_APPS:
    INSTALLED_APPS += ("passerelle_imio_apims_casier_judiciaire",)
    TENANT_APPS += ("passerelle_imio_apims_casier_judiciaire",)

if 'passerelle_imio_apims_certificats_population' not in INSTALLED_APPS:
    INSTALLED_APPS += ("passerelle_imio_apims_certificats_population",)
    TENANT_APPS += ("passerelle_imio_apims_certificats_population",)