import re

ASSET_STOCK = 'stock'
ASSET_ETF = 'etf'

# Asset types, as a tuple of tuples. Usable in Model ChoiceFields:
# (
#     ('stock', 'Stock'),
#     ('etf', 'etf'),
# )
ASSETS_BY_TYPE_CHOICES = (
    (ASSET_STOCK, ASSET_STOCK.title()),
    (ASSET_ETF, ASSET_ETF.title()),
)

# -------------------------------------------------------------------
# -------------------------------------------------------------------

# Regex patterns used to validate stock market tickers.
SYMBOL_PATTERN_DEFAULT = re.compile(r'^\w{1,4}$')
SYMBOL_PATTERN_LONG = re.compile(r'^[\w.]{1,7}$')

# -------------------------------------------------------------------
# -------------------------------------------------------------------

# United States Stock Market Exchanges.
ARCA_GROUP = 'ARCA'
ARCA_NAME = 'NYSE Arca'

AMEX_GROUP = 'AMEX'
AMEX_NAME = 'NYSE American'

NYSE_GROUP = 'NYSE'
NYSE_NAME = 'New York Stock Exchange'

BATS_GROUP = 'BATS'
BATS_NAME = 'BATS Global Markets'

NASDAQ_GROUP = 'NASDAQ'
NASDAQ_CAPITAL_MARKET_NAME = 'Nasdaq Capital Market'
NASDAQ_GLOBAL_MARKET_NAME = 'Nasdaq Global Market'
NASDAQ_GLOBAL_SELECT_NAME = 'Nasdaq Global Select'

OTC_GROUP = 'OTC'
OTC_QX_NAME = 'OTC QX'
OTC_QB_NAME = 'OTC QB'
OTC_PINK_SHEETS_NAME = 'OTC Pink Sheets'

# Nested mapping of exchange group to exchange name.
# Example:
#    {
#        'AMEX': ['NYSE American'],
#        'NYSE': ['New York Stock Exchange'],
#        'BATS': ['BATS Global Markets'],
#        'NASDAQ': [
#            'Nasdaq Capital Market',
#            ...
#        ],
#    }
EXCHANGES_BY_GROUP = {
    ARCA_GROUP: [ARCA_NAME],
    AMEX_GROUP: [AMEX_NAME],
    NYSE_GROUP: [NYSE_NAME],
    BATS_GROUP: [BATS_NAME],
    NASDAQ_GROUP: [
        NASDAQ_CAPITAL_MARKET_NAME,
        NASDAQ_GLOBAL_MARKET_NAME,
        NASDAQ_GLOBAL_SELECT_NAME,
    ],
    OTC_GROUP: [
        OTC_QX_NAME,
        OTC_QB_NAME,
        OTC_PINK_SHEETS_NAME,
    ]
}

# A flat mapping of exchange name to exchange group.
# Example:
#    {
#        "NYSE American": "AMEX",
#        "New York Stock Exchange": "NYSE",
#        "Nasdaq Capital Market": "NASDAQ",
#        "OTC QX": "OTC",
#        ...
#    }
EXCHANGES_BY_NAME = {
    name: group
    for group, names in EXCHANGES_BY_GROUP.items()
    for name in names
}

# A list of unique exchange names.
EXCHANGE_NAMES = list(EXCHANGES_BY_NAME.keys())

# Exchange names, as a tuple of tuples. Usable in Model ChoiceFields:
# (
#     ('NYSE American', 'NYSE American'),
#     ('New York Stock Exchange', 'New York Stock Exchange'),
#     ('Nasdaq Global Market', 'Nasdaq Global Market'),
#     ...
# )
EXCHANGES_BY_NAME_CHOICES = tuple((name, name) for name in EXCHANGE_NAMES)

# -------------------------------------------------------------------
# -------------------------------------------------------------------

ETF_LEVERAGE_NONE = 0

# A flat mapping of Etf leverage code to Etf leverage display.
ETF_LEVERAGE_BY_CODE = {
    4: '4x Quadruple-leveraged',
    3: '3x Triple-leveraged',
    2: '2x Double-leveraged',
    ETF_LEVERAGE_NONE: '',
    -2: '-2x Inverse Double-leveraged',
    -3: '-3x Inverse Triple-leveraged',
    -4: '-4x Inverse Quadruple-leveraged',
}

# Etf leverage types, as a tuple of tuples. Usable in Model ChoiceFields:
# (
#     (4, '4x Quadruple-leveraged'),
#     (3, '3x Triple-leveraged'),
#     (2, '2x Double-leveraged'),
#     ...
# )
ETF_LEVERAGE_BY_CODE_CHOICES = tuple(ETF_LEVERAGE_BY_CODE.items())

# -------------------------------------------------------------------
# -------------------------------------------------------------------

# ISO-3166 Country Codes.
# Ref: https://github.com/lukes/ISO-3166-Countries-with-Regional-Codes/blob/master/all/all.csv

COUNTRIES_BY_NAME = {
    'afghanistan': 'AF',
    'aland islands': 'AX',
    'albania': 'AL',
    'algeria': 'DZ',
    'american samoa': 'AS',
    'andorra': 'AD',
    'angola': 'AO',
    'anguilla': 'AI',
    'antarctica': 'AQ',
    'antigua and barbuda': 'AG',
    'argentina': 'AR',
    'armenia': 'AM',
    'aruba': 'AW',
    'australia': 'AU',
    'austria': 'AT',
    'azerbaijan': 'AZ',
    'bahamas': 'BS',
    'bahrain': 'BH',
    'bangladesh': 'BD',
    'barbados': 'BB',
    'belarus': 'BY',
    'belgium': 'BE',
    'belize': 'BZ',
    'benin': 'BJ',
    'bermuda': 'BM',
    'bhutan': 'BT',
    'bolivia': 'BO',
    'bonaire': 'BQ',
    'bosnia and herzegovina': 'BA',
    'botswana': 'BW',
    'bouvet island': 'BV',
    'brazil': 'BR',
    'british indian ocean territory': 'IO',
    'brunei darussalam': 'BN',
    'bulgaria': 'BG',
    'burkina faso': 'BF',
    'burundi': 'BI',
    'cabo verde': 'CV',
    'cambodia': 'KH',
    'cameroon': 'CM',
    'canada': 'CA',
    'cayman islands': 'KY',
    'central african republic': 'CF',
    'chad': 'TD',
    'chile': 'CL',
    'china': 'CN',
    'christmas island': 'CX',
    'cocos islands': 'CC',
    'colombia': 'CO',
    'comoros': 'KM',
    'congo': 'CG',
    'congo (democratic republic of the)': 'CD',
    'cook islands': 'CK',
    'costa rica': 'CR',
    "cote d'ivoire": 'CI',
    'croatia': 'HR',
    'cuba': 'CU',
    'curaçao': 'CW',
    'cyprus': 'CY',
    'czechia': 'CZ',
    'denmark': 'DK',
    'djibouti': 'DJ',
    'dominica': 'DM',
    'dominican republic': 'DO',
    'ecuador': 'EC',
    'egypt': 'EG',
    'el salvador': 'SV',
    'equatorial guinea': 'GQ',
    'eritrea': 'ER',
    'estonia': 'EE',
    'eswatini': 'SZ',
    'ethiopia': 'ET',
    'falkland islands': 'FK',
    'faroe islands': 'FO',
    'fiji': 'FJ',
    'finland': 'FI',
    'france': 'FR',
    'french guiana': 'GF',
    'french polynesia': 'PF',
    'french southern territories': 'TF',
    'gabon': 'GA',
    'gambia': 'GM',
    'georgia': 'GE',
    'germany': 'DE',
    'ghana': 'GH',
    'gibraltar': 'GI',
    'greece': 'GR',
    'greenland': 'GL',
    'grenada': 'GD',
    'guadeloupe': 'GP',
    'guam': 'GU',
    'guatemala': 'GT',
    'guernsey': 'GG',
    'guinea': 'GN',
    'guinea-bissau': 'GW',
    'guyana': 'GY',
    'haiti': 'HT',
    'heard island and mcdonald islands': 'HM',
    'holy see': 'VA',
    'honduras': 'HN',
    'hong kong': 'HK',
    'hungary': 'HU',
    'iceland': 'IS',
    'india': 'IN',
    'indonesia': 'ID',
    'iran': 'IR',
    'iraq': 'IQ',
    'ireland': 'IE',
    'isle of man': 'IM',
    'israel': 'IL',
    'italy': 'IT',
    'jamaica': 'JM',
    'japan': 'JP',
    'jersey': 'JE',
    'jordan': 'JO',
    'kazakhstan': 'KZ',
    'kenya': 'KE',
    'kiribati': 'KI',
    'north korea': 'KP',
    'south korea': 'KR',
    'kuwait': 'KW',
    'kyrgyzstan': 'KG',
    'lao': 'LA',
    'latvia': 'LV',
    'lebanon': 'LB',
    'lesotho': 'LS',
    'liberia': 'LR',
    'libya': 'LY',
    'liechtenstein': 'LI',
    'lithuania': 'LT',
    'luxembourg': 'LU',
    'macau': 'MO',
    'macedonia': 'MK',
    'madagascar': 'MG',
    'malawi': 'MW',
    'malaysia': 'MY',
    'maldives': 'MV',
    'mali': 'ML',
    'malta': 'MT',
    'marshall islands': 'MH',
    'martinique': 'MQ',
    'mauritania': 'MR',
    'mauritius': 'MU',
    'mayotte': 'YT',
    'mexico': 'MX',
    'micronesia': 'FM',
    'moldova': 'MD',
    'monaco': 'MC',
    'mongolia': 'MN',
    'montenegro': 'ME',
    'montserrat': 'MS',
    'morocco': 'MA',
    'mozambique': 'MZ',
    'myanmar': 'MM',
    'namibia': 'NA',
    'nauru': 'NR',
    'nepal': 'NP',
    'netherlands': 'NL',
    'new caledonia': 'NC',
    'new zealand': 'NZ',
    'nicaragua': 'NI',
    'niger': 'NE',
    'nigeria': 'NG',
    'niue': 'NU',
    'norfolk island': 'NF',
    'northern mariana islands': 'MP',
    'norway': 'NO',
    'oman': 'OM',
    'pakistan': 'PK',
    'palau': 'PW',
    'palestine': 'PS',
    'panama': 'PA',
    'papua new guinea': 'PG',
    'paraguay': 'PY',
    'peru': 'PE',
    'philippines': 'PH',
    'pitcairn': 'PN',
    'poland': 'PL',
    'portugal': 'PT',
    'puerto rico': 'PR',
    'qatar': 'QA',
    'réunion': 'RE',
    'romania': 'RO',
    'russian federation': 'RU',
    'rwanda': 'RW',
    'saint barthelemy': 'BL',
    'saint helena': 'SH',
    'saint kitts and nevis': 'KN',
    'saint lucia': 'LC',
    'saint martin': 'MF',
    'saint pierre and miquelon': 'PM',
    'saint vincent': 'VC',
    'samoa': 'WS',
    'san marino': 'SM',
    'sao tome and principe': 'ST',
    'saudi arabia': 'SA',
    'senegal': 'SN',
    'serbia': 'RS',
    'seychelles': 'SC',
    'sierra leone': 'SL',
    'singapore': 'SG',
    'sint maarten': 'SX',
    'slovakia': 'SK',
    'slovenia': 'SI',
    'solomon islands': 'SB',
    'somalia': 'SO',
    'south africa': 'ZA',
    'south georgia and the south sandwich islands': 'GS',
    'south sudan': 'SS',
    'spain': 'ES',
    'sri lanka': 'LK',
    'sudan': 'SD',
    'suriname': 'SR',
    'svalbard and jan mayen': 'SJ',
    'sweden': 'SE',
    'switzerland': 'CH',
    'syria': 'SY',
    'taiwan': 'TW',
    'tajikistan': 'TJ',
    'tanzania': 'TZ',
    'thailand': 'TH',
    'timor-leste': 'TL',
    'togo': 'TG',
    'tokelau': 'TK',
    'tonga': 'TO',
    'trinidad and tobago': 'TT',
    'tunisia': 'TN',
    'turkey': 'TR',
    'turkmenistan': 'TM',
    'turks and caicos islands': 'TC',
    'tuvalu': 'TV',
    'uganda': 'UG',
    'ukraine': 'UA',
    'united arab emirates': 'AE',
    'united kingdom': 'GB',
    'united states': 'US',
    'united states minor outlying islands': 'UM',
    'uruguay': 'UY',
    'uzbekistan': 'UZ',
    'vanuatu': 'VU',
    'venezuela': 'VE',
    'viet nam': 'VN',
    'british virgin islands': 'VG',
    'u.s. virgin islands': 'VI',
    'wallis and futuna': 'WF',
    'western sahara': 'EH',
    'yemen': 'YE',
    'zambia': 'ZM',
    'zimbabwe': 'ZW',
}

# Countries, as a tuple of tuples. Usable in Model ChoiceFields:
# (
#    ('BR', 'Brazil'),
#    ('FR', 'France'),
#    ('TW', 'Taiwan'),
#    ('US', 'United States')
#    ...
# )
#
COUNTRIES_BY_CODE_CHOICES = tuple(
    (v, k.title()) for k, v in COUNTRIES_BY_NAME.items())
