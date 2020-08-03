body {
    color: #f7f7f7;
}
.jumbotron {
    background-image: url("../images/nasa.jpg");
    background-size: 100% 100%;
    text-align: center;
}
button {
    background-color: blue;
    color: cornsilk;
} 


<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>UFO Finder</title>
    <link
      rel="stylesheet"
      href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css"
      integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm"
      crossorigin="anonymous"
    />
    <link rel="stylesheet" href="./css/style.css">
</head>
<body class="bg-dark">
    <div class="wrapper">
        <!-- Nav classes are specific to Bootstrap’s built-in styling; "navbar"-->
        <nav class="navbar navbar-dark bg-dark navbar-expand-lg">
            <a class="navbar-brand" href="index.html">UFO Sightings</a>
        </nav>
        <div class="jumbotron">
            <h1 class="display-4">The Truth Is Out There</h1>
        </div>
        <div class="container-fluid">
            <div class="row">
                <div class="col-md-4">
                    <h3>UFO Sightings: Fact or Fancy? <small>Ufologists Weigh In</small></h3>
                </div>
                <div class="col-md-8">
                    <p>
                        Are we alone in the universe? For millennia, humans have turned to the sky to answer this question. Now, thanks to research generously funded by W. Avy, a UFO-enthusiast and amateur ufologist, we can supplement our sky-searching with data analysis.<br><br>"The release of this analysis is well-timed: It coincides with the celebration of World UFO Day, which is a moment for ufologists around the world to connect, relax, and sample a range of UFO-themed snacks," said Dr. Ursula F. Olivier, the world's preeminent expert on circular sightings. "Citizen-scientists can be especially helpful in both cataloguing sightings—which is hugely helpful for us in our search for aliens—and in helping us celebrate the work that has already been done, such as this data visualization project, which will help us raise awareness of the ubiquity of sightings!"<br><br>Not everyone is ready to celebrate, however. Local CEO and vocal anti-alien activist V. Isualize reached out to our reporters to go on record as firmly opposed to any attempts to provide access to this data. "If there are aliens, they certainly would like to be left alone," she stated, before directing us to the Leave Aliens Alone (LAA) community engagement initiative she founded and funds.<br><br>So what do YOU think? Are we alone in the universe? Are aliens trying to contact us, or do they want to be left alone? Dig through the data yourself, and let us know what you see.
          
          
                      </p>
                </div>
            </div>
        </div>
        <div class="container-fluid">
            <div class="row">
                <div class="col-md-3">
                    <form class="bg-dark">
                        <p>Filter Search</p>
                        <ul class="list-group bg-dark">
                            <li class="list-group-item bg-dark">
                                <label for="date">Date</label>
                                <input type="text" placeholder="1/10/2010" id="datetime" />
                            </li>
                            <li class="list-group-item bg-dark">
                                <label for="city">City</label>
                                <input type="text" placeholder="" id="city" />
                            </li>
                            <li class="list-group-item bg-dark">
                                <label for="state">State</label>
                                <input type="text" placeholder="" id="state" />
                            </li>
                            <li class="list-group-item bg-dark">
                                <label for="country">Country</label>
                                <input type="text" placeholder="" id="country" />
                            </li>
                            <li class="list-group-item bg-dark">
                                <label for="shape">Shape</label>
                                <input type="text" placeholder="" id="shape" />
                            </li>
                            <li class="list-group-item bg-dark">
                                <button id="filter-btn" type="button" class="btn bg-dark" style="color:white;">Filter Table</button>
                                <button id="filter-btn" type="button" class="btn">Filter Table</button>
                            </li>
                        </ul>
                      </form>
                </div>
                <div class="col-md-9">
                    <table class="table table-striped">
                        <thead>
                          <tr>
                            <th>Date</th>
                            <th>City</th>
                            <th>State</th>
                            <th>Country</th>
                            <th>Shape</th>
                            <th>Duration</th>
                            <th>Comments</th>
                          </tr>
                        </thead>
                        <tbody></tbody>
                      </table>
                </div>
            </div>
        </div>
    </div>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/d3/4.11.0/d3.js"></script>
    <script src="./js/data.js"></script>
    <script src="./js/app.js"></script>
</body>
</html>