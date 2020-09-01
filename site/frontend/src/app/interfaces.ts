export interface Run {
    Id: number;
    PipeID: string;
    direction: string; // does this want to be number or string?
    Name?: string;
    Date?: Date;
    Driver?: string; // does this want to be an enum?
    lat?: number;
    long?: number;
    image?: HTMLImageElement;
    tag?: Tag[];
}

export interface Tag {
    locationNum: number;
    Lat: number;
    Longi: number;
    image?: HTMLImageElement;
    timeStamp?: number;
}

export interface numHash {
    [index: number]: boolean;
}