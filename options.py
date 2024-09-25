country_iso2_mapping = {
    'Albania': 'AL',
    'Andorra': 'AD',
    'Austria': 'AT',
    'Belarus': 'BY',
    'Belgium': 'BE',
    'Bosnia and Herzegovina': 'BA',
    'Bulgaria': 'BG',
    'Croatia': 'HR',
    'Cyprus': 'CY',
    'Czech Republic': 'CZ',
    'Denmark': 'DK',
    'Estonia': 'EE',
    'Finland': 'FI',
    'France': 'FR',
    'Germany': 'DE',
    'Greece': 'GR',
    'Hungary': 'HU',
    'Iceland': 'IS',
    'Ireland': 'IE',
    'Italy': 'IT',
    'Kosovo': 'XK',
    'Latvia': 'LV',
    'Liechtenstein': 'LI',
    'Lithuania': 'LT',
    'Luxembourg': 'LU',
    'Malta': 'MT',
    'Moldova': 'MD',
    'Monaco': 'MC',
    'Montenegro': 'ME',
    'Netherlands': 'NL',
    'North Macedonia': 'MK',
    'Norway': 'NO',
    'Poland': 'PL',
    'Portugal': 'PT',
    'Romania': 'RO',
    'Russia': 'RU',  # Note: ISO2 code for Russia is "RU," but it spans both Europe and Asia.
    'San Marino': 'SM',
    'Serbia': 'RS',
    'Slovakia': 'SK',
    'Slovenia': 'SI',
    'Spain': 'ES',
    'Sweden': 'SE',
    'Switzerland': 'CH',
    'Ukraine': 'UA',  # Note: ISO2 code for Ukraine is "UA," but it spans both Europe and Asia.
    'United Kingdom': 'GB',
    'Vatican City': 'VA'
}


legend_content = """
<div class="small-caps">
    <p><span class="unit">k<sub>W</sub>h</span>&emsp;: kilowatt-hour, a unit of energy equivalent to one kilowatt of power used for one hour.</p>
    <p><span class="unit">m<sub>W</sub>h</span>&emsp;: megawatt-hour, a unit of energy equivalent to one megawatt of power used for one hour. 1 mWh = 1000 kWh.</p>

<table>
    <tr>
        <th>Indicator</th>
        <th>Consumption Rate-Range</th>
    </tr>
    <tr>
        <td>KWH_LT1000</td>
        <td><span class="unit">k<sub>W</sub>h</span> 1000 or less</td>
    </tr>
    <tr>
        <td>KWH2500-4999</td>
        <td><span class="unit">k<sub>W</sub>h</span> 2500-4999</td>
    </tr>
    <tr>
        <td>KWH5000-14999</td>
        <td><span class="unit">k<sub>W</sub>h</span> 5000-14999</td>
    </tr>
    <tr>
        <td>KWH_GE15000</td>
        <td><span class="unit">k<sub>W</sub>h</span> 15000 or over</td>
    </tr>
    <tr>
        <td>MWH20-499</td>
        <td><span class="unit">m<sub>W</sub>h</span> 20-499</td>
    </tr>
    <tr>
        <td>MWH2000-19999</td>
        <td><span class="unit">m<sub>W</sub>h</span> 2000-19999</td>
    </tr>
    <tr>
        <td>MWH20000-69999</td>
        <td><span class="unit">m<sub>W</sub>h</span> 20000-69999</td>
    </tr>
    <tr>
        <td>MWH500-1999</td>
        <td><span class="unit">m<sub>W</sub>h</span> 500-1999</td>
    </tr>
    <tr>
        <td>MWH70000-149999</td>
        <td><span class="unit">m<sub>W</sub>h</span> 70000-149999</td>
    </tr>
    <tr>
        <td>MWH_LE149999</td>
        <td><span class="unit">m<sub>W</sub>h</span> 149999 or over</td>
    </tr>
    <tr>
        <td>MWH_LT20</td>
        <td><span class="unit">m<sub>W</sub>h</span> 20 or less</td>
    </tr>
</table>
</div>
"""

