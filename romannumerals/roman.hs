import qualified Data.Map as Map

conversions =
    [(4, ["", "M", "MM", "MMM"]),
     (3, ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]),
     (2, ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]),
     (1, ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"])
    ]
conversion_map = Map.fromList(conversions)