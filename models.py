allowed_states = {
    3: "pre_venta", 4: "en_venta", 5: "vendido"
}


class Inmueble:
    def __init__(
        self,
        id,
        address,
        city,
        price,
        description,
        year,
        state,
    ):
        self.id = id
        self.address = address
        self.city = city
        self.state = allowed_states.get(state)
        self.price = price
        self.description = description
        self.year = year

    def __iter__(self):
        yield 'id', self.id
        yield 'address', self.address
        yield 'city', self.city
        yield 'state', self.state
        yield 'price', self.price
        yield 'description', self.description
        yield 'year', self.year


def inmueble_factory(parameters):
    inmueble = Inmueble(
        id=parameters.get('id'),
        address=parameters.get('address'),
        city=parameters.get('city'),
        state=parameters.get('state'),
        price=parameters.get('price'),
        description=parameters.get('description'),
        year=parameters.get('year')
    )
    return inmueble
