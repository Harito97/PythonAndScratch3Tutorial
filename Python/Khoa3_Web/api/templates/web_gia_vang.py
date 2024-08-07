import random

def generate_gold_stats():
    """
    Generates random gold price statistics.
    """
    gold_stats = {
        "SJC_HN_buy": round(random.uniform(55.5, 56.5), 1),
        "SJC_HN_sell": round(random.uniform(56.0, 57.0), 1),
        "SJC_HCM_buy": round(random.uniform(55.7, 56.7), 1),
        "SJC_HCM_sell": round(random.uniform(56.2, 57.2), 1),
        "DOJI_HN_buy": round(random.uniform(55.6, 56.6), 1),
        "DOJI_HN_sell": round(random.uniform(56.1, 57.1), 1),
        "DOJI_HCM_buy": round(random.uniform(55.8, 56.8), 1),
        "DOJI_HCM_sell": round(random.uniform(56.3, 57.3), 1),
        "TG_buy": round(random.uniform(1850, 1900), 1),
        "TG_sell": round(random.uniform(1860, 1910), 1)
    }
    return gold_stats

# Generate the gold price statistics
gold_stats = generate_gold_stats()

# Generate the HTML table
HTML_FORM = """<!DOCTYPE html>
<html lang="en">

<head>
    <title>Tổng hợp thông tin giá vàng</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.16.0/umd/popper.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
</head>

<body>

    <div class="container-fluid">
        <!--#2a3477-->
        <div class="row bg-primary justify-content-center align-items-center" style="height: 80px">
            <h1 style="color:White; font-family:calibri">Trang tổng hợp thông tin giá vàng trong nước</h1>
        </div>
        <div class="row" style="height: 40px">
        </div>
        <div class="col-8 offset-2">
            <h2 class="font-weight-bold" style="text-align:center">Số liệu thống kê</h2>
            <br>
            <table class="table table-bordered">
                <thead>
                    <tr>
                        <th scope="col"></th>
                        <th scope="col">Mua vào</th>
                        <th scope="col">Bán ra</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <th scope="row">SJC Hà Nội</th>
                        <td>{SJC_HN_buy}</td>
                        <td>{SJC_HN_sell}</td>
                    </tr>
                    <tr>
                        <th scope="row">SJC HCM</th>
                        <td>{SJC_HCM_buy}</td>
                        <td>{SJC_HCM_sell}</td>
                    </tr>
                    <tr>
                        <th scope="row">DOJI Hà Nội</th>
                        <td>{DOJI_HN_buy}</td>
                        <td>{DOJI_HN_sell}</td>
                    </tr>
                    <tr>
                        <th scope="row">DOJI HCM</th>
                        <td>{DOJI_HCM_buy}</td>
                        <td>{DOJI_HCM_sell}</td>
                    </tr>
                    <tr>
                        <th scope="row">Thế giới</th>
                        <td>{TG_buy}</td>
                        <td>{TG_sell}</td>
                    </tr>
                </tbody>
            </table>

        </div>
    </div>
</body>

</html>
""".format(**gold_stats)