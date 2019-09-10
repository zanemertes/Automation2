tariffs = {'TEC': 'Economy Class Tab2_Beitrag_berechnen',
           'TPC': 'Premium Economy Class Tab2_Beitrag_berechnen',
           'TBC': 'Business Class Tab2_Beitrag_berechnen',
           'TFC': 'First Class Tab2_Beitrag_berechnen',
           }
tariff_components = {'PVB': 'Pflegepflichtversicherung für Beamte',
                     'BAZ': 'Grundbaustein Ambulant und Zahn',
                     'BS': 'Grundbaustein Stationär',
                     'BBEC': 'Bündel Economy Class',
                     'BBPC': 'Bündel Premium Economy Class',
                     'BBBC': 'Bündel Business Class',
                     'BBFC': 'Bündel First Class',
                     'BEC': 'Zusatzbaustein Economy Class',
                     'BFC': 'Zusatzbaustein First Class',
                     'BBC': 'Zusatzbaustein Business Class',
                     'BEK': 'Beitragsentlastungskomponente',
                     'KT': 'Krankentagegeldversicherung',
                     }
tariff_postfixes = {'A': 'Arbeitnehmer',
                    'S': 'Selbstständige',
                    }
beihilfe_tariff_postfixes = {'A': 'Ausbildung',
                             'W': 'Beamtenanwärter / Beamte auf Widerruf',
                             'K': 'Kurzstufe'
                             }
tariff_components.update({'KTA':  "{0} {1}".format(tariff_components['KT'], tariff_postfixes['A']),
                          'KTS':  "{0} {1}".format(tariff_components['KT'], tariff_postfixes['S']),

                          'BAZA': "{0} {1}".format(tariff_components['BAZ'], beihilfe_tariff_postfixes['A']),
                          'BAZK': "{0} {1}".format(tariff_components['BAZ'], beihilfe_tariff_postfixes['K']),
                          'BAZW': "{0} {1}".format(tariff_components['BAZ'], beihilfe_tariff_postfixes['W']),

                          'BSA': "{0} {1}".format(tariff_components['BS'], beihilfe_tariff_postfixes['A']),
                          'BSK': "{0} {1}".format(tariff_components['BS'], beihilfe_tariff_postfixes['K']),
                          'BSW': "{0} {1}".format(tariff_components['BS'], beihilfe_tariff_postfixes['W']),

                          'BECA': "{0} {1}".format(tariff_components['BEC'], beihilfe_tariff_postfixes['A']),
                          'BECW': "{0} {1}".format(tariff_components['BEC'], beihilfe_tariff_postfixes['W']),

                          'BFCA': "{0} {1}".format(tariff_components['BFC'], beihilfe_tariff_postfixes['A']),
                          'BFCW': "{0} {1}".format(tariff_components['BFC'], beihilfe_tariff_postfixes['W']),

                          'BBCA': "{0} {1}".format(tariff_components['BBC'], beihilfe_tariff_postfixes['A']),
                          'BBCK': "{0} {1}".format(tariff_components['BBC'], beihilfe_tariff_postfixes['K']),
                          'BBCW': "{0} {1}".format(tariff_components['BBC'], beihilfe_tariff_postfixes['W'])
                          })


class TariffComponent(object):
    # TODO: Add support for the levels
    def __init__(self, abbr: str or None, level: int=100, price: float=0.0, currency: str="€"):
        if level not in range(0, 101):
            log("The level '{0}' lies outside the 0-100 range. Check code!".format(level))
            raise ValueError
        self.level = level

        self.abbr = abbr
        # this is to enable custom __init__ methods in children classes
        if abbr is not None:
            if abbr in tariff_components:
                self.name = tariff_components[abbr]
            else:
                log("The abbreviation '{0}' is not supported. Check code!".format(abbr))
                raise ValueError

        if price is not None:
            self.price = round(price, 2)

        self.currency = currency


class TariffBundle(TariffComponent):
    _type = 'Bundle'
    components = {}

    # TODO: Add the 'Gesetzlichen Zuschlag' as bool property and float property
    def __init__(self, abbr: str or None, price: float, components: {str: TariffComponent} or None=None):
        super().__init__(abbr=abbr)

        # this is the 'parent' saved as component
        self.append_component(TariffComponent(abbr=abbr, price=price))

        if components is not None and components is not {}:
            for component in components.values():
                self.append_component(component=component)
            log("{3} price '{2}' = '{0} {1}' ".format(self.price, self.currency, self.abbr, self._type))
        else:
            self.components = {}

    def append_component(self, component: TariffComponent):
        self.components.update({component.abbr: component})
        self.price += round(component.price, 2)
        self.price = round(self.price, 2)
        log("Adding price '{0} {1}' from component '{2}'\t{3} total = {4}".
            format(component.price, component.currency, component.abbr, self._type, self.price))

    def remove_component(self, component: TariffComponent):
        if component.abbr in self.components:
            del self.components[component.abbr]
            self.price -= round(component.price, 2)
            self.price = round(self.price, 2)
            log("Deducting price '{0} {1}' from component '{2}'\t{3} total = {4}".
                format(component.price, component.currency, component.abbr, self._type, self.price))
        else:
            log("The component {0} was not in the list.".format(component.abbr))


class Tariff(TariffBundle):
    _type = 'Tab2_Beitrag_berechnen'
    components = {}

    def __init__(self, abbr: str, components: {str: TariffComponent or TariffBundle} or None = None,
                 short_name: str or None=None):
        super().__init__(abbr=None, price=0.0, components=components)

        self.short_name = short_name

        self.abbr = abbr
        # this is to enable custom __init__ methods in children classes
        if abbr is not None:
            if abbr in tariffs:
                self.name = tariffs[abbr]
            else:
                log("The abbreviation '{0}' is not supported. Check code!".format(abbr))
                raise ValueError

    # def get_component(self, name: str) -> TariffComponent or TariffBundle:
    #     """
    #     :param name:
    #     :return: TariffComponent with a matching abbreviation, or (full) name
    #     """
    #     if self.components is None or self.components is []:
    #         log("The components list was None or empty. Check code!")
    #         raise ValueError
    #     for c in self.components:
    #         if c.abbr == name or c.name == name:
    #             return c

    def compare(self, tariff: 'Tab2_Beitrag_berechnen', soft: bool=True) -> bool:
        # COMPLETE PRICE
        _c = [self.price, tariff.price]
        result = p_assert(assertion=_c[0] == _c[1], soft=soft,
                          message="Comparing Tab2_Beitrag_berechnen-totals:\n{0} == {1}".format(_c[0], _c[1]))
        # COMPONENTS PRICES
        for _a, _comp in self.components.items():
            t_c = tariff.components[_a]
            _c = [_comp.price, t_c.price]
            result = result and p_assert(assertion=_c[0] == _c[1], soft=soft,
                                         message="Comparing Tab2_Beitrag_berechnen component {2}:\n{0} == {1}".format(_c[0], _c[1], _a))
        return result
