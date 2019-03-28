>>> lows = set([0, 1, 2, 3, 4])
>>> odds = set([1, 3, 5, 7, 9])
>>> lows - odds    # lows.difference(odds)와 동등
{0, 2, 4}
>>> lows & odds    # lows.intersection(odds)와 동등
{1, 3}
>>> lows <= odds    # lows.issubset(odds)와 동등
False
>>> lows >= odds    # lows.issuperset(odds)와 동등
False 
>>> lows | odds    # lows.union(odds)와 동등
{0, 1, 2, 3, 4, 5, 7, 9} 
>>> lows ^ odds    # lows.symmetric_difference(odds)와 동등
{0, 2, 4, 5, 7, 9} 