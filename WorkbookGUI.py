import tkinter as tk, Workbook as wb


class WorkbookGUI:
    def __init__(self, workbook):
        self.workbook = workbook;
        window = tk.Tk();
        window.mainloop()


if __name__ == "__main__":
    debug_workbook_gui = WorkbookGUI(wb.Workbook())
    input()
