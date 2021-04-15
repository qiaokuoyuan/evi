import copy
from functools import reduce


class Evi:
    def __init__(self, focal_elements, bpas: list = []):
        self.delta = .0000001

        assert abs(1 - sum(bpas)) < self.delta

        self.focal_elements = [set(f if isinstance(f, list) or isinstance(f, set) or isinstance(f, tuple) else [f, ])
                               for f in focal_elements]
        self.bpas = bpas

    def normalization(self):
        self.bpas = [b / sum(self.bpas) for b in self.bpas]

    def combine(self, e):
        assert isinstance(e, Evi)
        assert len(e.focal_elements) == len(e.bpas)
        assert len(self.focal_elements) == len(self.bpas)

        for self_focal_element in self.focal_elements:
            if self_focal_element not in e.focal_elements:
                e.focal_elements.append(self_focal_element)
                e.bpas.append(self.delta)
        e.normalization()

        bpas = []
        focal_elements = []

        def add_bpa(focal_element, bpa):
            for i in range(len(focal_elements)):
                if Evi.focal_elemt_same(focal_elements[i], focal_element):
                    bpas[i] = bpas[i] + bpa
                    bpa = 0

            if bpa > 0:
                bpas.append(bpa)
                focal_elements.append(focal_element)

        for i in range(len(self.focal_elements)):
            for j in range(len(e.focal_elements)):

                f1 = self.focal_elements[i]
                f2 = e.focal_elements[j]

                f = f1 & f2

                if len(f) > 0:
                    add_bpa(f, self.bpas[i] * e.bpas[j])

        bpas = [b / sum(bpas) for b in bpas]

        return Evi(focal_elements, bpas)

    def max_focal_element(self):

        max_bpa = max(self.bpas)

        for i in range(len(self.bpas)):
            if self.bpas[i] == max_bpa:
                return self.focal_elements[i]

    def __str__(self):
        evi_string = ["P(%s):%s" % (str(self.focal_elements[i]), str(self.bpas[i])) for i in
                      range(len(self.focal_elements))]

        return reduce(lambda x, y: x + ";" + y, evi_string)

    @classmethod
    def combine_list(cls, *evis):
        assert len(evis) > 0
        if len(evis) == 1:
            return evis[0]
        else:
            e1 = copy.deepcopy(evis[0])
            for e in evis[1:]:
                e1 = e1.combine(e)
            return e1

    @classmethod
    def focal_elemt_same(cls, focal_elemt_1, focal_elemt_2):
        if len(focal_elemt_1) != len(focal_elemt_2):
            return False
        focal_elemt_1 = set(focal_elemt_1)
        focal_elemt_2 = set(focal_elemt_2)
        for f in focal_elemt_1:
            if f not in focal_elemt_2:
                return False

        return True


__all__ = [Evi]
