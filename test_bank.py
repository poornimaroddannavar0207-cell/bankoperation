from bank import bankOperation

def test_deposit():
    totalBalance, updatedBalance = bankOperation(200000, 30000, 0)

    assert totalBalance == 230000
    assert updatedBalance == 230000

def test_withdrawal():
    totalBalance, updatedBalance = bankOperation(100000, 40000, 10000)

    assert totalBalance == 140000
    assert updatedBalance == 130000

def test_anyamount():
    totalBalance, updatedBalance = bankOperation(150000, 0, 15000)

    assert totalBalance == 150000
    assert updatedBalance == 135000

def bankOperation(initialBalance, deposit, withdrawal):
    totalBalance = initialBalance + deposit
    updatedBalance = totalBalance - withdrawal

    return totalBalance, updatedBalance