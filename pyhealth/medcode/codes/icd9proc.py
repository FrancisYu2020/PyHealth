from pyhealth.medcode.inner_map import InnerMap


class ICD9PROC(InnerMap):

    def __init__(self, **kwargs):
        super(ICD9PROC, self).__init__(vocabulary="ICD9PROC", **kwargs)

    def preprocess(self, code):
        """Normalizes ICD9PROC code."""
        if "." in code:
            return code
        assert len(code) >= 2
        if len(code) == 2:
            return code
        return code[:2] + "." + code[2:]


if __name__ == "__main__":
    code_sys = ICD9PROC(refresh_cache=True)
    code_sys.stat()
    print("81.01" in code_sys)
    print(code_sys.lookup("01.31"))
    print(code_sys.get_ancestors("01.31"))
    print(code_sys.get_descendants("01"))
