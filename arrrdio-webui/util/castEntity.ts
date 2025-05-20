export interface TrackInfo {
    title: string,
    album: string,
    artist: string,
    thumbnailUrl: string
}

export interface CastEntity {
  address: string,
  odesliEntityId: string,
  _trackInfo: TrackInfo
}

