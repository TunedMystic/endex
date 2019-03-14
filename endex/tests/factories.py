from decimal import Decimal
import random

import faker
import factory

from endex.constants import (
    # ASSETS_BY_TYPE_CHOICES,
    # COUNTRIES_BY_CODE_CHOICES,
    # ETF_LEVERAGE_BY_CODE_CHOICES,
    EXCHANGE_NAMES
)
from endex.models import (
    Exchange
)


ALPHABET = 'ABCDEFGHOJKLMNOPQRSTUVWXYZ'
SECTORS = ['Energy', 'Materials', 'Industrials', 'Consumer Discretionary', 'Consumer Staples', 'Health Care', 'Financials', 'Information Technology', 'Telecommunication Services', 'Utilities', 'Real Estate']
INDUSTRIES = ['Oil & Gas Production', 'Semiconductors', 'Specialty Foods', 'Building Products', 'Real Estate', 'Building Materials', 'Accident & Health Insurance', 'Computer Software: Programming', 'Data Processing', 'Transportation Services', 'Life Insurance', 'Consumer Specialties', 'Oil Refining/Marketing', 'Finance: Consumer Services', 'Office Equipment/Supplies/Services', 'Biotechnology: Laboratory Analytical Instruments', 'Clothing/Shoe/Accessory Stores', 'Agricultural Chemicals', 'Biotechnology: Biological Products (No Diagnostic Substances)', 'Advertising', 'n/a', 'Air Freight/Delivery Services', 'Motor Vehicles', 'Power Generation', 'Aluminum', 'Professional Services', 'Coal Mining', 'Farming/Seeds/Milling', 'Pollution Control Equipment', 'Railroads', 'Industrial Machinery/Components', 'Movies/Entertainment', 'Computer Software: Prepackaged Software', 'Other Specialty Stores', 'Auto Manufacturing', 'Automotive Aftermarket', 'Real Estate Investment Trusts', 'Television Services', 'Electronic Components', 'Steel/Iron Ore', 'Meat/Poultry/Fish', 'Water Supply', 'Electric Utilities: Central', 'Biotechnology: Commercial Physical & Biological Resarch', 'Medical/Dental Instruments', 'Package Goods/Cosmetics', 'EDP Services', 'Major Banks', 'Medical Electronics', 'Food Distributors', 'Retail: Computer Software & Peripheral Equipment', 'Savings Institutions', 'Aerospace', 'Computer Communications Equipment', 'Other Consumer Services', 'Textiles', 'Plastic Products', 'Investment Managers', 'Biotechnology: Electromedical & Electrotherapeutic Apparatus', 'RETAIL: Building Materials', 'Major Chemicals', 'Metal Fabrications', 'Oilfield Services/Equipment', 'Ophthalmic Goods', 'Paper', 'Radio And Television Broadcasting And Communications Equipment', 'Food Chains', 'Banks', 'Restaurants', 'Consumer Electronics/Appliances', 'Rental/Leasing Companies', 'Environmental Services', 'Diversified Financial Services', 'Ordnance And Accessories', 'Industrial Specialties', 'Medical Specialities', 'Homebuilding', 'Integrated oil Companies', 'Property-Casualty Insurers', 'Engineering & Construction', 'Biotechnology: In Vitro & In Vivo Diagnostic Substances', 'Broadcasting', 'Telecommunications Equipment', 'Precision Instruments', 'Computer peripheral equipment', 'Hotels/Resorts', 'Department/Specialty Retail Stores', 'Recreational Products/Toys', 'Shoe Manufacturing', 'Newspapers/Magazines', 'Specialty Chemicals', 'Home Furnishings', 'Investment Bankers/Brokers/Service', 'Commercial Banks', 'Construction/Ag Equipment/Trucks', 'Forest Products', 'Hospital/Nursing Management', 'Diversified Electronic Products', 'Packaged Foods', 'Services-Misc. Amusement & Recreation', 'Containers/Packaging', 'Consumer Electronics/Video Chains', 'Marine Transportation', 'Major Pharmaceuticals', 'Diversified Commercial Services', 'Miscellaneous manufacturing industries', 'Apparel', 'Beverages (Production/Distribution)', 'Publishing', 'Multi-Sector Companies', 'Finance/Investors Services', 'Mining & Quarrying of Nonmetallic Minerals (No Fuels)', 'Miscellaneous', 'Catalog/Specialty Distribution', 'Business Services', 'Military/Government/Technical', 'Specialty Insurers', 'Medical/Nursing Services', 'Books', 'Other Pharmaceuticals', 'Precious Metals', 'Natural Gas Distribution', 'Trucking Freight/Courier Services', 'Computer Manufacturing', 'Finance Companies', 'Building operators', 'Auto Parts:O.E.M.', 'Electrical Products']
ISSUERS = ['AdvisorShares', 'Alpha Architect', 'ALPS', 'ARK', 'ArrowShares Investment Adviser', 'Barclays iPath', 'Blackrock', 'Calamos Investments', 'Cambria', 'Charles Schwab', 'Citigroup', 'Columbia', 'Credit Suisse', 'CSOP', 'Deutsche Banks', 'Diamond Hill', 'Direxion', 'Emerging Global Shares', 'Elkhorn', 'ETF Managers Group', 'ETF Securities', 'Fidelity', 'First Trust', 'FQF Trust', 'Franklin ETF Trust', 'Global X', 'Goldman Sachs', 'GreenHaven', 'Guggenheim', 'Highland Capital Management', 'Horizons', 'HSBC', 'Huntington Strategy Shares', 'IndexIQ', 'Invesco PowerShares', 'John Hancock', 'JP Morgan', 'KraneShares', 'Lattice Strategies', 'Legg Mason', 'LocalShares', 'Millington Securities Inc', 'Montage Managers', 'Northern Trust', 'Oppenheimer Funds', 'Pacer Financial', 'PIMCO', 'Precidian', 'ProShares', 'Reality Shares', 'Recon Capital', 'Renaissance Capital', 'Royal Bank of Canada', 'State Street', 'Swedish Export Credit', 'Teucrium', 'The Principal Financial Group', 'TrimTabs Asset Management', 'UBS', 'US Bancorp', 'US Commodity Funds', 'US Global Investors', 'USCF Advisers', 'Van Eck', 'Vanguard', 'VelocityShares', 'Victory Capital Management', 'Virtus', 'WisdomTree']
CATEGORIES = ['California Munis', 'Corporate Bonds', 'Emerging Markets Bonds', 'Government Bonds', 'High Yield Bonds', 'Inflation-Protected Bonds', 'International Government Bonds', 'Money Market', 'Mortgage Backed Securities', 'National Munis', 'New York Munis', 'Preferred Stock/Convertible Bonds', 'Total Bond Market', 'Agricultural Commodities', 'Commodities', 'Metals', 'Oil & Gas', 'Precious Metals', 'Currency', 'Diversified Portfolio', 'Target Retirement Date', 'All Cap Equities', 'Alternative Energy Equities', 'Asia Pacific Equities', 'Building & Construction', 'China Equities', 'Commodity Producers Equities', 'Communications Equities', 'Consumer Discretionary Equities', 'Consumer Staples Equities', 'Emerging Markets Equities', 'Energy Equities', 'Europe Equities', 'Financials Equities', 'Foreign Large Cap Equities', 'Foreign Small & Mid Cap Equities', 'Global Equities', 'Health & Biotech Equities', 'Industrials Equities', 'Japan Equities', 'Large Cap Blend Equities', 'Large Cap Growth Equities', 'Large Cap Value Equities', 'Latin America Equities', 'MLPs', 'Materials', 'Mid Cap Blend Equities', 'Mid Cap Growth Equities', 'Mid Cap Value Equities', 'Small Cap Blend Equities', 'Small Cap Growth Equities', 'Small Cap Value Equities', 'Technology Equities', 'Transportation Equities', 'Utilities Equities', 'Volatility Hedged Equity', 'Water Equities', 'Hedge Fund', 'Long-Short', 'Inverse Bonds', 'Inverse Commodities', 'Inverse Equities', 'Inverse Volatility', 'Leveraged Bonds', 'Leveraged Commodities', 'Leveraged Currency', 'Leveraged Equities', 'Leveraged Multi-Asset', 'Leveraged Real Estate', 'Leveraged Volatility', 'Global Real Estate', 'Real Estate', 'Volatility']

fake = faker.Faker()


def random_symbol():
    return ''.join(random.choice(ALPHABET) for i in range(random.choice([3, 4])))


def make_exchanges():
    Exchange.insert_many([
        {'name': exchange_name}
        for exchange_name in EXCHANGE_NAMES
    ]).execute()


def random_exchange_id():
    # return Exchange._meta.database.execute_sql('SELECT e.id FROM exchange e TABLESAMPLE SYSTEM_ROWS(1);').fetchone()[0]
    return Exchange._meta.database.execute_sql('SELECT e.id FROM exchange e ORDER BY RANDOM() LIMIT 1;').fetchone()[0]


# def random_leverage():
#     return random.choice(ETF_LEVERAGE_BY_CODE_CHOICES)[0]


# def random_sector():
#     return SECTORS[random.randint(0, len(SECTORS) - 1)]


# def random_industry():
#     return INDUSTRIES[random.randint(0, len(INDUSTRIES) - 1)]


# def random_issuer():
#     return ISSUERS[random.randint(0, len(ISSUERS) - 1)]


# def random_category():
#     return CATEGORIES[random.randint(0, len(CATEGORIES) - 1)]


# def random_big_number():
#     return Decimal(random.randrange(100_000_000, 8_000_000_000))


# def random_percent():
#     return Decimal(str(random.random())).quantize(Decimal('0.00000'))


# def random_country_code():
#     return COUNTRIES_BY_CODE_CHOICES[random.randint(0, len(COUNTRIES_BY_CODE_CHOICES) - 1)][0]


# def random_phone():
#     return '-'.join(str(random.randint(100, 999)) for _ in range(3)) + str(random.randint(0, 9))


# def random_cusip():
#     return fake.sha1()[:9]


# def random_isin(cusip):
#     return random_country_code() + cusip + str(random.randint(0, 9))


# def random_tags():
#     return fake.words(nb=random.randint(0, 4))


# MARKET_INDEX_BY_TYPE = {
#     'stock': lambda: None,
#     'etf': lambda: random_symbol()
# }


# SECTOR_BY_TYPE = {
#     'stock': lambda: random_sector(),
#     'etf': lambda: None
# }


# INDUSTRY_BY_TYPE = {
#     'stock': lambda: random_industry(),
#     'etf': lambda: None
# }


# ISSUER_BY_TYPE = {
#     'stock': lambda: None,
#     'etf': lambda: random_issuer(),
# }


# CATEGORY_BY_TYPE = {
#     'stock': lambda: None,
#     'etf': lambda: random_category()
# }


# SHARES_FLOAT_BY_TYPE = {
#     'stock': lambda: random_big_number(),
#     'etf': lambda: None
# }


# SHARES_OUTSTANDING_BY_TYPE = {
#     'stock': lambda: random_big_number(),
#     'etf': lambda: None
# }


# INST_HELD_BY_TYPE = {
#     'stock': lambda: random_big_number(),
#     'etf': lambda: None
# }


# INSIDER_HELD_BY_TYPE = {
#     'stock': lambda: random_big_number(),
#     'etf': lambda: None
# }


# LEVERAGE_BY_TYPE = {
#     'stock': lambda: None,
#     'etf': lambda: random_leverage()
# }


# TOTAL_ASSETS_BY_TYPE = {
#     'stock': lambda: None,
#     'etf': lambda: random_big_number()
# }


# ADDRESS_BY_TYPE = {
#     'stock': lambda: AddressFactory(),
#     'etf': lambda: None
# }


# CONTACT_BY_TYPE = {
#     'stock': lambda: ContactFactory(),
#     'etf': lambda: None
# }


# class AddressFactory(factory.mongoengine.MongoEngineFactory):
#     class Meta:
#         model = Address

#     street = factory.Faker('street_address')
#     city = factory.Faker('city')
#     zipcode = factory.Faker('zipcode')
#     country = factory.LazyFunction(random_country_code)


# class ContactFactory(factory.mongoengine.MongoEngineFactory):
#     class Meta:
#         model = Contact

#     email = factory.Faker('email')
#     phone = factory.LazyFunction(random_phone)


# class AssetFactory(factory.mongoengine.MongoEngineFactory):
#     class Meta:
#         model = Asset

#     asset_hash = factory.Faker('sha1')

#     type = factory.LazyFunction(lambda: random.choice(ASSETS_BY_TYPE_CHOICES)[0])
#     symbol = factory.LazyFunction(random_symbol)
#     name = factory.Faker('company')
#     exchange = factory.LazyFunction(random_exchange)
#     market_index = factory.LazyAttribute(lambda o: MARKET_INDEX_BY_TYPE[o.type]())
#     cusip = factory.LazyFunction(random_cusip)
#     isin = factory.LazyAttribute(lambda o: random_isin(o.cusip))

#     description = factory.LazyFunction(lambda: ' '.join(fake.paragraphs()))
#     website = factory.Faker('url')
#     date_founded = factory.Faker('date_between', start_date="-30y", end_date="-20y")
#     date_listed = factory.Faker('date_between', start_date="-19y", end_date="-1y")

#     sector = factory.LazyAttribute(lambda o: SECTOR_BY_TYPE[o.type]())
#     industry = factory.LazyAttribute(lambda o: INDUSTRY_BY_TYPE[o.type]())
#     issuer = factory.LazyAttribute(lambda o: ISSUER_BY_TYPE[o.type]())
#     category = factory.LazyAttribute(lambda o: CATEGORY_BY_TYPE[o.type]())
#     tags = factory.LazyFunction(random_tags)

#     shares_float = factory.LazyAttribute(lambda o: SHARES_FLOAT_BY_TYPE[o.type]())
#     shares_outstanding = factory.LazyAttribute(lambda o: SHARES_OUTSTANDING_BY_TYPE[o.type]())
#     held_by_institutions = factory.LazyAttribute(lambda o: INST_HELD_BY_TYPE[o.type]())
#     held_by_insiders = factory.LazyAttribute(lambda o: INSIDER_HELD_BY_TYPE[o.type]())

#     leverage = factory.LazyFunction(random_leverage)
#     total_assets = factory.LazyFunction(random_big_number)

#     address = factory.LazyAttribute(lambda o: ADDRESS_BY_TYPE[o.type]())
#     contact = factory.LazyAttribute(lambda o: CONTACT_BY_TYPE[o.type]())


from endex.db import get_db
from endex.models import Etf, Stock


class PeeweeOptions(factory.base.FactoryOptions):
    def _build_default_options(self):
        return super(PeeweeOptions, self)._build_default_options() + [
            factory.base.OptionDefault('database', None, inherit=True),
        ]


class PeeweeModelFactory(factory.base.Factory):
    _options_class = PeeweeOptions

    class Meta:
        abstract = True

    @classmethod
    def _create(cls, target_class, *args, **kwargs):
        # db = cls._meta.database
        obj = target_class.create(**kwargs)
        return obj


class StockFactory(PeeweeModelFactory):
    class Meta:
        model = Stock
        database = get_db()

    symbol = factory.LazyFunction(random_symbol)
    name = factory.Faker('company')
    exchange_id = factory.LazyFunction(random_exchange_id)


class EtfFactory(PeeweeModelFactory):
    class Meta:
        model = Etf
        database = get_db()

    symbol = factory.LazyFunction(random_symbol)
    name = factory.Faker('company')
    exchange_id = factory.LazyFunction(random_exchange_id)
