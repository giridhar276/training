# 22. Polymorphism using Duck Typing
# Different classes can have same method name.
# Python checks behavior, not exact type.

class PDFReport:
    def generate(self):
        print("Generating PDF report")

class ExcelReport:
    def generate(self):
        print("Generating Excel report")

class HTMLReport:
    def generate(self):
        print("Generating HTML report")

def create_report(report_object):
    report_object.generate()

create_report(PDFReport())
create_report(ExcelReport())
create_report(HTMLReport())
