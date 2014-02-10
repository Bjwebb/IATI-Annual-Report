from collections import defaultdict

elements = [
    "reporting-org",
    "other-identifier",
    "title",
    "description",
    "activity-status",
    "activity-date",
    "activity-date[@type='start-planned']",
    "activity-date[@type='start-actual']",
    "activity-date[@type='end-planned']",
    "activity-date[@type='end-actual']",
    "contact-info",
    "participating-org[@role='Funding']",
    "participating-org[@role='Extending']",
    "participating-org[@role='Implementing']",
    "participating-org[@role='Accountable']",
    "recipient-country",
    "recipient-region",
    "location",
    "location/name",
    "location/location-type",
    "location/description",
    "location/administrative",
    "location/coordinates",
    "location/gazetteer-entry",
    "sector",
    "policy-marker",
    "collaboration-type",
    "default-flow-type",
    "default-finance-type",
    "default-aid-type",
    "default-tied-status",
    "budget",
    "budget/period-start",
    "budget/period-end",
    "budget/value",
    "planned-disbursement",
    "planned-disbursement/period-start",
    "planned-disbursement/period-end",
    "planned-disbursement/value",
    "transaction",
    "transaction/value",
    "transaction/description",
    "transaction/transaction-type",
    "transaction/transaction-type[@code='C']",
    "transaction/transaction-type[@code='D']",
    "transaction/transaction-type[@code='E']",
    "transaction/transaction-type[@code='IF']",
    "transaction/transaction-type[@code='LR']",
    "transaction/transaction-type[@code='R']",
    "transaction/provider-org",
    "transaction/receiver-org",
    "transaction/transaction-date",
    "transaction/flow-type",
    "transaction/aid-type",
    "transaction/finance-type",
    "transaction/tied-status",
    "transaction/disbursement-channel",
    "document-link",
    "activity-website",
    "related-activity",
    "conditions",
    "conditions/condition",
    "result",
    "result/indicator",
    "result/indicator/baseline",
    "result/indicator/period",
    "result/indicator/period/period-start",
    "result/indicator/period/period-end",
    "result/indicator/period/target",
    "result/indicator/period/actual",
    "contact-info/organisation",
    "contact-info/person-name",
    "contact-info/telephone",
    "contact-info/email",
    "contact-info/mailing-address",
    "legacy-data",
    ]

def returns_numberdict(f):
    """ Dectorator for dictionaries of integers. """
    def wrapper(self, *args, **kwargs):
        if self.blank:
            return defaultdict(int)
        else:
            out = f(self, *args, **kwargs)
            if out is None: return {}
            else: return out
    return wrapper

class ActivityStats(object):
    blank = False

    @returns_numberdict
    def elements_annual_report(self):
        return {element:len(self.element.xpath(element)) for element in elements}

class ActivityFileStats(object):
    pass

class PublisherStats(object):
    pass

class OrganisationFileStats(object):
    pass

class OrganisationStats(object):
    pass
