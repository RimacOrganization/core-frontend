from excel.util.utils import ExcelWorkbook
import sys, os
class AutoFitRange:
    def __init__(self) -> None:
        pass
    def auto_fit_range(sheet:str,path:str) -> None:
        '''
        Function "auto_fit_range" writes a range of values in 
        an indicated worksheet.
        Input(s):
            sheet:      Name of the worksheet that will 
                        be activated.
            path:       File path to do the actions.
        '''
        try:
            wb = ExcelWorkbook.workbook(path)
        except Exception as exc:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc, fname, exc_tb.tb_lineno)
            raise
        else:
            try:
                ws = ExcelWorkbook.active_worksheet(wb,sheet)
            except Exception as exc:
                exc_type, exc_obj, exc_tb = sys.exc_info()
                fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                print(exc, fname, exc_tb.tb_lineno)
                raise ValueError("info incorrect")
            else:
                for col in ws.columns:
                    max_length = 0
                    column = col[0].column_letter 
                    for cell in col:
                        try: # Necessary to avoid error on empty cells
                            if len(str(cell.value)) > max_length:
                                max_length = len(str(cell.value))
                        except:
                            pass
                    adjusted_width = (max_length + 0.97) 
                    ws.column_dimensions[column].width = adjusted_width
                ExcelWorkbook.save_workbook(wb,path)    