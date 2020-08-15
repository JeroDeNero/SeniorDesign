export interface Run {
    videoID: number;
    pipeID: string;
    direction: string; // does this want to be number or string?
    name?: string;
    date?: Date;
    driver?: string; // does this want to be an enum?
    lat?: number;
    long?: number;
    image?: HTMLImageElement;
    tag?: Tag[];
}

export interface Tag {
    locationNum: number;
    lat: number;
    long: number;
    image?: HTMLImageElement;
    timeStamp?: number;
}

export interface numHash {
    [index: number]: boolean;
}