from .codenames import (
    account_manager,
    administration,
    ae,
    ae_review,
    auditor,
    celery_manager,
    clinic,
    data_manager,
    data_query,
    everyone,
    export,
    lab,
    lab_view,
    pharmacy,
    pii,
    pii_view,
    rando,
    site_data_manager,
    tmg,
)
from .group_names import (
    AE,
    AE_REVIEW,
    ACCOUNT_MANAGER,
    ADMINISTRATION,
    AUDITOR,
    CELERY_MANAGER,
    CLINIC,
    DATA_MANAGER,
    DATA_QUERY,
    EVERYONE,
    EXPORT,
    LAB,
    LAB_VIEW,
    PHARMACY,
    PII,
    PII_VIEW,
    RANDO,
    SITE_DATA_MANAGER,
    TMG,
)

default_codenames_by_group = {
    AE: ae,
    AE_REVIEW: ae_review,
    ACCOUNT_MANAGER: account_manager,
    ADMINISTRATION: administration,
    AUDITOR: auditor,
    CELERY_MANAGER: celery_manager,
    CLINIC: clinic,
    DATA_MANAGER: data_manager,
    DATA_QUERY: data_query,
    EVERYONE: everyone,
    EXPORT: export,
    LAB: lab,
    LAB_VIEW: lab_view,
    PHARMACY: pharmacy,
    PII: pii,
    PII_VIEW: pii_view,
    RANDO: rando,
    SITE_DATA_MANAGER: site_data_manager,
    TMG: tmg,
}
