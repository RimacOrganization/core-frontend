from excel.util.utils import ExcelWorkbook
import sys, os
class AppendRange:
    def __init__(self) -> None:
        pass
    @staticmethod
    def append_range(sheet:str,data_table:list[list],path:str,exclude_headers:bool = False) -> None:
        '''
        Function "append_range" append values in 
        an indicated worksheet.
        Input(s):
            sheet:              Name of the worksheet that will 
                                be activated.
            data_table:         Values to be inserted.
            path:               File path to do the actions.
            exclude_headers:    Indicate if the headers will be
                                inserted.
        Output(s):
        '''
        try:
            wb = ExcelWorkbook.workbook(path)
        except Exception as exc:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            raise
        else:
            try:
                ws = ExcelWorkbook.active_worksheet(wb,sheet)
            except Exception as exc:
                exc_type, exc_obj, exc_tb = sys.exc_info()
                fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                raise
            else:
                if (exclude_headers==True):
                    data_table.pop(0)
                else:
                    pass
                for row in data_table:
                    ws.append(row)
                    ExcelWorkbook.save_workbook(wb,path)