INSERT INTO Video 
(Name, Tagged, DateTaken, DriverName)
VALUES
("xyz", 1, NOW(), "FRED");

INSERT INTO Video 
(Name, Tagged, DateTaken, DriverName)
VALUES
("zyx", 1, NOW(), "Tom");

INSERT INTO Video 
(Name, DateTaken, DriverName)
VALUES
("xy", NOW(), "FRED");

INSERT INTO Video 
(Name, DateTaken, DriverName)
VALUES
("xz", NOW(), "FRED");

INSERT INTO Video 
(Name, DateTaken, DriverName)
VALUES
("yz", NOW(), "FRED");

INSERT INTO Video 
(DateTaken, DriverName)
VALUES
(NOW(), "FRED");

INSERT INTO Video 
(DateTaken, DriverName)
VALUES
(NOW(), "Tom");

INSERT INTO TaggedLocs 
(Longi, Lat, VideoTime)
VALUES
(1, 1, 15);

INSERT INTO TaggedLocs 
(Longi, Lat, VideoTime)
VALUES
(-1, 1, 30);

INSERT INTO TaggedLocs 
(Longi, Lat, VideoTime)
VALUES
(1, -1, 45);

INSERT INTO TaggedLocs 
(Longi, Lat, VideoTime)
VALUES
(-1, -1, 60);

INSERT INTO VideoToTags 
(VideoID, TagID)
VALUES
(1,4);

INSERT INTO VideoToTags 
(VideoID, TagID)
VALUES
(1,1);

INSERT INTO VideoToTags 
(VideoID, TagID)
VALUES
(3,2);

INSERT INTO VideoToTags 
(VideoID, TagID)
VALUES
(5,3);

INSERT INTO Pipe 
(Id, Lat, Longi, Direction)
VALUES
('abc', 1, 1, 1);

INSERT INTO Pipe 
(Id, Lat, Longi, Direction)
VALUES
('ab', 1, -1, 1);

INSERT INTO Pipe 
(Id, Lat, Longi, Direction)
VALUES
('a', 1, 1, -1);
