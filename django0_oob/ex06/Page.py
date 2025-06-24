from elem import Elem, Text
from elements import Html, Head, Body, Title, Meta, Img, \
                    Table, Th, Tr, Td, Ul, Ol, Li, \
                    H1, H2, P, Div, Span, Hr, Br


class Page:
    def __init__(self, elem: Elem):
        self.elem = elem

    def _test_elem(self, elem):
        match elem:
            case Html() | Head() | Body() | Title() | Meta() | Img() | \
                    Table() | Th() | Tr() | Td() | Ul() | Ol() | Li() | \
                    H1() | H2() | P() | Div() | Span() | Hr() | Br() | Text():
                return True
            case _:
                return False

    def _test_html(self, elem: Html):
        if len(elem.content) != 2:
            return False
        if type(elem.content[0]) is not Head and\
           type(elem.content[1]) is not Body:
            return False
        return True

    def _test_head(self, elem: Head):
        if len(elem.content) != 1:
            return False
        if type(elem.content[0]) is not Title:
            return False
        return True

    def _test_body_div(self, elem: Body | Div):
        for e in elem.content:
            match e:
                case H1() | H2() | Div() | Table() | Ul() | Ol() \
                        | Span() | Text():
                    continue
                case _:
                    print(f'here {type(e)}')
                    return False
        return True

    def _test_only_one_Text(self, elem: Title | H1 | H2 | Li | Th | Td):
        if len(elem.content) != 1:
            return False
        if type(elem.content[0]) is not Text:
            return False
        return True

    def _test_P(self, elem: P):
        for e in elem.content:
            if type(e) is not Text:
                return False
        return True

    def _test_Span(self, elem: Span):
        for e in elem.content:
            if type(e) is not Text and\
              type(e) is not P:
                return False
        return True

    def _test_Ol_Ul(self, elem: Ol | Ul):
        if len(elem.content) < 1:
            return False

        for e in elem.content:
            if type(e) is not Li:
                return False

        return True

    def _test_Tr(self, elem):
        if len(elem.content) < 1:
            return False

        curr_type = type(elem.content[0])
        for e in elem.content:
            if type(e) is not curr_type:
                return False

        return True

    def _test_Table(self, elem):
        for e in elem.content:
            if type(e) is not Tr:
                return False

        return True

    def _test_element(self, elem):
        if not self._test_elem(elem):
            return False

        match elem:
            case Html():
                return self._test_html(elem)
            case Head():
                return self._test_head(elem)
            case Body() | Div():
                return self._test_body_div(elem)
            case Title() | H1() | H2() | Li() | Th() | Td():
                return self._test_only_one_Text(elem)
            case P():
                return self._test_P(elem)
            case Span():
                return self._test_Span(elem)
            case Ol() | Ul():
                return self._test_Ol_Ul(elem)
            case Tr():
                return self._test_Tr(elem)
            case Table():
                return self._test_Table(elem)
            case _:
                print(f'UHHH how did we get here type = {type(elem)}')
                return False

        return True

    def _verify(self, elem):

        if not self._test_element(elem):
            return False
        for e in elem.content:
            match e:
                case Text():
                    continue
                case _:
                    if not self._verify(e):
                        print(type(e))
                        return False

        return True

    def is_valid(self):
        # something something

        return self._verify(self.elem)

    def __str__(self):
        if type(self.elem) is Html:
            return ("<!DOCTYPE html>\n" + str(self.elem))
        return (str(self.elem))

    def write_to_file(self, path):
        try:
            file = open(path, 'w')
        except Exception:
            print(f'could not open file {path}')

        file.write(str(self))
        file.close()


def print_test(target: Page, toBe: bool):
    print("================START===============")
    print(str(target))
    print("===============IS_VALID=============")
    assert target.is_valid() == toBe
    print("{:^36s}".format(str(target.is_valid())))
    print("=================END================")


def test_Table():
    print("\n%{:=^34s}%\n".format("Table"))
    target = Page(Table())
    print_test(target, True)
    target = Page(
        Table(
            [
                Tr(),
            ]))
    print_test(target, False)
    target = Page(
        Table(
            [
                H1(
                    Text("Hello World!")
                ),
            ]))
    print_test(target, False)


def test_Tr():
    print("\n%{:=^34s}%\n".format("Tr"))
    target = Page(Tr())
    print_test(target, False)
    target = Page(
        Tr(
            [
                Th(Text("title")),
                Th(Text("title")),
                Th(Text("title")),
                Th(Text("title")),
                Th(Text("title")),
            ]))
    print_test(target, True)
    target = Page(
        Tr(
            [
                Td(Text("content")),
                Td(Text("content")),
                Td(Text("content")),
                Td(Text("content")),
                Td(Text("content")),
                Td(Text("content")),
            ]))
    print_test(target, True)
    target = Page(
        Tr(
            [
                Th(Text("title")),
                Td(Text("content")),
            ]))
    print_test(target, False)


def test_Ul_OL():
    print("\n%{:=^34s}%\n".format("Ul_OL"))
    target = Page(
        Ul()
    )
    print_test(target, False)
    target = Page(
        Ol()
    )
    print_test(target, False)
    target = Page(
        Ul(
            Li(
                Text('test')
            )
        )
    )
    print_test(target, True)
    target = Page(
        Ol(
            Li(
                Text('test')
            )
        )
    )
    print_test(target, True)
    target = Page(
        Ul([
            Li(
                Text('test')
            ),
            Li(
                Text('test')
            ),
        ])
    )
    print_test(target, True)
    target = Page(
        Ol([
            Li(
                Text('test')
            ),
            Li(
                Text('test')
            ),
        ])
    )
    print_test(target, True)
    target = Page(
        Ul([
            Li(
                Text('test')
            ),
            H1(
                Text('test')
            ),
        ])
    )
    print_test(target, False)
    target = Page(
        Ol([
            Li(
                Text('test')
            ),
            H1(
                Text('test')
            ),
        ])
    )
    print_test(target, False)


def test_Span():
    print("\n%{:=^34s}%\n".format("Span"))
    target = Page(
        Span()
    )
    print_test(target, True)
    target = Page(
        Span([
            Text("Hello?"),
            P(Text("World!")),
        ])
    )
    print_test(target, True)
    target = Page(
        Span([
            H1(Text("World!")),
        ])
    )
    print_test(target, False)


def test_P():
    print("\n%{:=^34s}%\n".format("P"))
    target = Page(
        P()
    )
    print_test(target, True)
    target = Page(
        P([
            Text("Hello?"),
        ])
    )
    print_test(target, True)
    target = Page(
        P([
            H1(Text("World!")),
        ])
    )
    print_test(target, False)


def test_Title_H1_H2_Li_Th_Td():
    print("\n%{:=^34s}%\n".format("H1_H2_Li_Th_Td"))
    for c in [H1, H2, Li, Th, Td]:
        target = Page(
            c()
        )
        print_test(target, False)
        target = Page(
            c([
                Text("Hello?"),
            ])
        )
        print_test(target, True)
        target = Page(
            c([
                H1(Text("World!")),
            ])
        )
        print_test(target, False)
        target = Page(
            c([
                Text("Hello?"),
                Text("Hello?"),
            ])
        )
        print_test(target, False)


def test_Body_Div():
    print("\n%{:=^34s}%\n".format("Body_Div"))
    for c in [Body, Div]:
        target = Page(
            c()
        )
        print_test(target, True)
        target = Page(
            c([
                Text("Hello?"),
            ])
        )
        print_test(target, True)
        target = Page(
            c([
                H1(Text("World!")),
            ])
        )
        print_test(target, True)
        target = Page(
            c([
                Text("Hello?"),
                Span(),
            ])
        )
        print_test(target, True)
        target = Page(
            c([
                Html(),
                c()
            ])
        )
        print_test(target, False)


def test_Title():
    print("\n%{:=^34s}%\n".format("Title"))
    target = Page(
        Title()
    )
    print_test(target, False)
    target = Page(
        Title([
            Title(Text("Hello?")),
        ])
    )
    print_test(target, True)
    target = Page(
        Title([
            Title(Text("Hello?")),
            Title(Text("Hello?")),
        ])
    )
    print_test(target, False)


def test_Html():
    print("\n%{:=^34s}%\n".format("Html"))
    target = Page(
        Html()
    )
    print_test(target, False)
    target = Page(
        Html([
            Head([
                Title(Text("Hello?")),
            ]),
            Body([
                H1(Text("Hello?")),
            ])
        ])
    )
    print_test(target, True)
    target = Page(
        Html(
            Div()
        )
    )
    print_test(target, False)


def test_Elem():
    print_test(Page(Elem()), False)


def test_write_to_file(target: Page, path: str):
    print("================START===============")
    print(str(target))
    print("==========WRITE_TO_FILE=============")
    target.write_to_file(path)
    print("{:^36s}".format(path))
    print("=================END================")


def test():
    test_Table()
    test_Tr()
    test_Ul_OL()
    test_Span()
    test_P()
    test_Title_H1_H2_Li_Th_Td()
    test_Body_Div()
    test_Html()
    test_Elem()
    test_write_to_file(
        Page(Html([Head(Title(Text("hello world!"))),
             Body(H1(Text("HELLO WORLD!")))])),
        "test_write_to_file.html")


if __name__ == "__main__":
    test()
