CREATE TABLE Video (
  Id int unsigned not null auto_increment,
  Name varchar(32),
  VideoLoc varchar(512),
  VideoClipLoc varchar(512),
  Tagged smallint,
  DateTaken datetime not null,
  DriverName varchar(32),
  
  primary key (Id)
);

CREATE TABLE TaggedLocs(
  Id int unsigned not null auto_increment,
  Longi smallint not null,
  Lat smallint not null,
  VideoTime smallint not null,
  ImageLoc varchar(512),

  primary key (Id)
);

CREATE TABLE HighlightedZones (
  Id int unsigned not null auto_increment,
  XPos int not null,
  YPos int not null,
  raduis int not null,

  primary key (Id)
);

CREATE Table Pipe (
  Id varchar(128) not null,
  Lat smallint,
  Longi smallint,
  Direction varchar(8),

  primary key (Id)
);

CREATE TABLE RoughLocation (
  Id int not null auto_increment,
  Name varchar(64) not null,
  Lat smallint not null,
  Longi smallint not null,
  raduis smallint not null,

  primary key (Id)
);

CREATE TABLE VideoToTags (
  VideoID int unsigned not null,
  TagID int unsigned not null,

  primary key (VideoID, TagID),

  foreign key (VideoID)
          references Video(Id),

  foreign key (TagID)
          references TaggedLocs(Id)
);

CREATE TABLE TagToHighlights (
  LocationId int unsigned not null,
  HighlightId int unsigned not null,

  primary key (LocationId, HighlightId),

  foreign key (LocationId)
          references TaggedLocs(Id),

  foreign key (HighlightId)
          references HighlightedZones(Id)
);

CREATE TABLE PipeToVid0 (
  VideoID int unsigned not null,
  PipeID varchar(128) not null,

  primary key (VideoID, PipeID),

  foreign key (VideoID)
          references Video(Id),

  foreign key (PipeID)
          references Pipe(Id)
);

CREATE TABLE PipeToRoughLoc (
  PipeID varchar(128) not null,
  RoughLocId int  not null,

  primary key (PipeID, RoughLocId),

  foreign key (PipeID)
          references Pipe(Id),

  foreign key (RoughLocId)
          references RoughLocation(Id)
);