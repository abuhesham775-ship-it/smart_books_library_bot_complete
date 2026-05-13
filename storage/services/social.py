from db.models.social import SocialComment, SocialPost
from schemas.social import SocialCommentCreate, SocialCommentRead, SocialPostCreate, SocialPostRead
from services.common import CRUDService

post_service = CRUDService[SocialPost, SocialPostCreate, SocialPostCreate](SocialPost)
comment_service = CRUDService[SocialComment, SocialCommentCreate, SocialCommentCreate](SocialComment)
