def user_profile_path(instance, filename):
    return'user_{0}/{1}'.format(instance.profile.user.id, filename)